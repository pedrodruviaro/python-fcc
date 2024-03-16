months = {
    'Jan': 'January',
    'Mar': 'March',
}

print(months['Jan'])

print(months.get("Mar"))

print(months.get("Fev", 'Invalid key')) # use a default value if "Fev" not exists