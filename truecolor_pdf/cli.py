import argparse
import asyncio
import sys
from .converter import run_conversion

def main():
    parser = argparse.ArgumentParser(description="Convert Colab .ipynb to PDF with true colors.")
    parser.add_argument("input", help="The input .ipynb file.")
    
    args = parser.parse_args()
    
    if not args.input.endswith('.ipynb'):
        print("Error: Input file must be a .ipynb file.")
        sys.exit(1)
        
    try:
        asyncio.run(run_conversion(args.input))
    except KeyboardInterrupt:
        print("\nConversion cancelled.")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
