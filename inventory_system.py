"""
Inventory Management System

This module manages stock items by adding, removing, saving, and loading
inventory data. It demonstrates best practices for Python coding standards,
security, and error handling.
"""

import json
import logging
from datetime import datetime
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format=(
        "%(asctime)s - %(levelname)s - %(message)s"
    ),
)

# Global variable for storing inventory data
STOCK_DATA = {}


def add_item(item="default", qty=0, logs=None):
    """Add a specified quantity of an item to the inventory."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning(
            "Invalid input types for add_item: item=%s, qty=%s",
            item,
            qty,
        )
        return

    STOCK_DATA[item] = STOCK_DATA.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item, qty):
    """Remove a specified quantity of an item from the inventory."""
    try:
        if item not in STOCK_DATA:
            logging.warning(
                "Attempted to remove non-existent item: %s", item
            )
            return

        STOCK_DATA[item] -= qty
        if STOCK_DATA[item] <= 0:
            del STOCK_DATA[item]
            logging.info("Removed item completely: %s", item)
        else:
            logging.info("Removed %d of %s", qty, item)
    except KeyError as e:
        logging.error("KeyError while removing item: %s", e)
    except ValueError as e:
        logging.error("Invalid value in remove_item: %s", e)


def get_qty(item):
    """Return the quantity of a specified item."""
    return STOCK_DATA.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict):
                STOCK_DATA.clear()
                STOCK_DATA.update(data)
                logging.info(
                    "Inventory loaded successfully from %s",
                    file_path,
                )
            else:
                logging.warning("Invalid data format in %s", file_path)
    except FileNotFoundError:
        logging.warning("File not found: %s", file_path)
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON: %s", e)
    except OSError as e:
        logging.error("OS error while loading file: %s", e)


def save_data(file_path="inventory.json"):
    """Save inventory data to a JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(STOCK_DATA, file, indent=4)
        logging.info("Inventory saved successfully to %s", file_path)
    except (OSError, TypeError) as e:
        logging.error("Failed to save inventory: %s", e)


def print_data():
    """Display the current inventory items and their quantities."""
    print("Items Report:")
    for item, qty in STOCK_DATA.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items with quantities below the given threshold."""
    return [item for item, qty in STOCK_DATA.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory system usage."""
    add_item("apple", 10)
    add_item("banana", 5)
    add_item("orange", 2)

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    logging.info("Program execution completed.")


if __name__ == "__main__":
    main()
