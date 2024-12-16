# List files that are staged for commit
# for file in $(git diff --cached --name-only); do
#     echo "=== Contents of $file ==="
#     git diff --cached "$file"
#     echo "Press Enter to see next file (Ctrl+C to exit)..."
#     read
# done

# Define color codes
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Loop through untracked files
for file in $(git ls-files --others --exclude-standard); do
    echo "=== Contents of $file ==="
    echo -e "${GREEN}$(cat "$file")${NC}"
    echo "Press Enter to see next file (Ctrl+C to exit)..."
    read
done