import pandas as pd
from app.database.db import SessionLocal
from app.models.models import MenuItem

def load_menu_from_excel(excel_path: str):
    db = SessionLocal()

    # Clear existing menu
    db.query(MenuItem).delete()
    db.commit()

    sheets = pd.read_excel(excel_path, sheet_name=None)

    for category, df in sheets.items():
        df.columns = [col.strip().lower() for col in df.columns]

        # Detect columns safely
        item_col = None
        price_col = None
        desc_col = None

        for col in df.columns:
            if "item" in col or "name" in col:
                item_col = col
            elif "price" in col or "cost" in col:
                price_col = col
            elif "description" in col or "desc" in col:
                desc_col = col

        if not item_col or not price_col:
            print(f"⚠️ Skipping sheet '{category}' (missing required columns)")
            continue

        for _, row in df.iterrows():
            db.add(
                MenuItem(
                    item_name=str(row[item_col]).strip(),
                    category=category,
                    description=str(row[desc_col]).strip() if desc_col else "",
                    price=float(row[price_col])
                )
            )

    db.commit()
    db.close()

    print("✅ Restaurant menu loaded from Excel successfully.")
