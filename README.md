```markdown
# 🛍️ Discount Calculator

A simple Python program that calculates the final price after applying a discount, with a minimum discount threshold.

## ✨ Features
- 🧮 Calculates discounted prices
- ⚡ Only applies discounts of 20% or higher
- 💰 Maintains original price for smaller discounts
- 🖥️ Clean and user-friendly interface
- 💵 Proper currency formatting

## 🚀 How to Use
1. Run the program:
```bash
python discount_calculator.py
```
2. Enter the original price when prompted
3. Enter the discount percentage
4. View the result showing either the discounted price or original price

## 📝 Example Output
```
Enter the original price: $100
Enter the discount percentage: 25
Final price after 25% discount: $75.00
```

```
Enter the original price: $50
Enter the discount percentage: 15  
No discount applied. Original price: $50.00
```

## 🛠️ Requirements
- Python 3.x (no external dependencies)

## 💡 Learning Objectives
- Function creation with parameters
- Conditional statements (if/else)
- Mathematical operations
- User input handling
- String formatting for currency

## 📁 Project Structure
```
discount-calculator/
├── discount_calculator.py    # Main program file
└── README.md                # Documentation
```

## 🔧 Customization
You can easily modify the minimum discount threshold by changing the `20` in the condition:
```python
if discount_percent >= 20:  # Change this value
```

---

Perfect for learning basic Python functions and conditional logic! 💻
```
