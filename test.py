import os
import shutil

# Paths
source_root = 'data/raw'
target_root = 'data'

splits = ['train', 'test']
classes = ['coffee', 'matcha']

# Create new directory structure
for split in splits:
    for cls in classes:
        dest_dir = os.path.join(target_root, split, cls)
        os.makedirs(dest_dir, exist_ok=True)

        # Source directory: data/raw/{cls}/{split}
        src_dir = os.path.join(source_root, cls, split)
        if not os.path.exists(src_dir):
            print(f"Skipping missing folder: {src_dir}")
            continue

        # Move files
        for filename in os.listdir(src_dir):
            src_path = os.path.join(src_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dest_path)

print("✅ Dataset restructuring complete.")
