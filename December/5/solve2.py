# Function to read the file and return the rules and updates
def read_file(file_path):
    with open(file_path, 'r') as file:
        document_body_text = file.read()
    # Split the document body text into rules and updates based on two newlines
    rules, updates = [section.strip().split("\n") for section in document_body_text.split("\n\n")]
    return rules, updates

# Create a lookup table for each set of numbers in the format:
# sort(x, y): aocOrder(x, y)
def process_rules(rules):
    rules_json = {}
    for rule in rules:
        rule_data = list(map(int, rule.split("|")))
        sorted_key = "|".join(map(str, sorted(rule_data)))
        rules_json[sorted_key] = rule_data
    return rules_json

# Function to sort the updates based on rules and check for changes
def process_updates(updates, original_updates, rules_json):
    total_sum = 0
    for index, update in enumerate(updates):
        # Sort
        list_ = list(map(int, update.split(",")))

        # Sort the list based on the custom rules
        list_.sort(key=lambda x: (
            next(
                (order[0] if order[0] == x else order[1])
                for rule in [list(sorted([x, y])) for x, y in zip(list_, list_[1:])]
                if (order := rules_json.get("|".join(map(str, rule)))) is not None
            ),
            0  # Provide a fallback value (0) in case no matching rule is found
        ))

        # Join the list into a comma-separated string
        list_ = ",".join(map(str, list_))

        # Compare to original
        if list_ != original_updates[index]:
            split = list_.split(",")
            total_sum += int(split[len(split) >> 1])  # Integer division by 2

    return total_sum

# Main function to process the file
def main(file_path):
    rules, updates = read_file(file_path)
    rules_json = process_rules(rules)
    original_updates = updates[:]
    result = process_updates(updates, original_updates, rules_json)
    print("Final sum:", result)

# Provide the file path to your input file
file_path = 'December/5/data.txt'  # Replace with the actual file path
main(file_path)