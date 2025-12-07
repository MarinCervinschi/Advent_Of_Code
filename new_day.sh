#!/bin/zsh

YEAR_DIR="$(dirname "$0")/2025"
LAST_DAY=$(ls -d "$YEAR_DIR"/day_* 2>/dev/null | sort -V | tail -1 | grep -oE '[0-9]+$')

if [ -z "$LAST_DAY" ]; then
    NEXT_DAY=1
else
    NEXT_DAY=$((10#$LAST_DAY + 1))
fi

NEXT_DAY_FORMATTED=$(printf "%02d" $NEXT_DAY)
DAY_DIR="$YEAR_DIR/day_$NEXT_DAY_FORMATTED"

mkdir -p "$DAY_DIR"

cat > "$DAY_DIR/main.py" << 'EOF'
def part_1(data):
    pass


def part_2(data):
    pass



def get_data(file_path):
    with open(file_path, "r") as file:
        data = [row.strip() for row in file]
    return data

if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    data = get_data(PATH / "puzzle.txt")
    part_1(data)
    part_2(data)
EOF

# Create empty notes files
touch "$DAY_DIR/puzzle.txt"

echo "Created day_$NEXT_DAY_FORMATTED in $YEAR_DIR"
