import pandas as pd
import sqlite3
import os
import re
from tkinter import Tk, filedialog, messagebox

def select_directory():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Select a Folder with csv Files")

def get_table_name_from_filename(filename):
    name = os.path.splitext(filename)[0]
    match = re.match(r"(.+)_\d{4}$", name)
    return match.group(1) if match else None

def get_table_columns(cursor, table_name):
    cursor.execute(f"PRAGMA table_info('{table_name}')")
    return [info[1] for info in cursor.fetchall()]

def table_exists(cursor, table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None

def process_csv_file(cursor, conn, file_path, table_name):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ Could not read {file_path}: {e}")
        return

    if df.empty:
        print(f"⚠️ Skipped empty file: {file_path}")
        return

    if table_exists(cursor, table_name):
        existing_cols = get_table_columns(cursor, table_name)
        incoming_cols = list(df.columns)

        if incoming_cols != existing_cols:
            print(f"⚠️ Column mismatch in table '{table_name}'. Skipping {os.path.basename(file_path)}.")
            print(f"Expected: {existing_cols}")
            print(f"Found:    {incoming_cols}")
        else:
            df.to_sql(table_name, conn, if_exists='append', index=False)
            print(f"✅ Appended to '{table_name}' from {file_path}")
    else:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"🆕 Created table '{table_name}' from {file_path}")

def process_folder(folder, cursor, conn):
    print(f"\n📁 Processing folder: {folder}")
    csv_files = [
        f for f in os.listdir(folder)
        if f.lower().endswith(('.csv')) and os.path.isfile(os.path.join(folder, f))
    ]

    if not csv_files:
        print(f"⚠️ No csv files found in: {folder}")
        return

    for file in csv_files:
        full_path = os.path.join(folder, file)
        table_name = get_table_name_from_filename(file)
        if table_name:
            process_csv_file(cursor, conn, full_path, table_name)
        else:
            print(f"❌ Ignored file not matching pattern: {file}")

def main():
    db_path = "freight_db.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        while True:
            folder = select_directory()
            if not folder:
                break
            process_folder(folder, cursor, conn)

            # Use a GUI prompt instead of input() to avoid freezing
            proceed = messagebox.askyesno("Continue?", "Do you want to select another folder?")
            if not proceed:
                break

    finally:
        conn.commit()
        conn.close()
        print("\n✅ All done. Database saved to:", db_path)

if __name__ == "__main__":
    main()
