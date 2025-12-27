import os
import re

def unfuck_links():
    root_dir = os.getcwd()
    
    # Pattern to find nested image tags: ![text](prefix![text2](url)suffix)
    # We want to keep the innermost one and preserve the path if possible, 
    # but usually the nesting is just a duplication.
    # Actually, let's look for: ![any](anything_containing_assets/![any](assets/any))
    
    # More general pattern: ![...]( ... ![...](...) ... )
    nested_pattern = re.compile(r'!\[[^\]]*\]\(([^)]*(!\[[^\]]*\]\([^)]+\))[^)]*)\)')

    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs: dirs.remove('.git')
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                while True:
                    m = nested_pattern.search(new_content)
                    if not m:
                        break
                    
                    # Group 1 is the inner content of the outer ( )
                    # Group 2 is the inner ![...](...)
                    # We want to replace the whole outer ![...](...) with the inner one.
                    # HOWEVER, we might need to preserve some relative pathing if it was prefixed.
                    # But my script just prefixed with assets_rel.
                    
                    # Let's see: ![browserdiagram.jpg](../../assets/![browserdiagram.jpg](../../assets/browserdiagram.jpg))
                    # Group 1: ../../assets/![browserdiagram.jpg](../../assets/browserdiagram.jpg)
                    # Group 2: ![browserdiagram.jpg](../../assets/browserdiagram.jpg)
                    
                    # We should just replace the whole match with Group 2.
                    start, end = m.span()
                    new_content = new_content[:start] + m.group(2) + new_content[end:]

                if new_content != content:
                    print(f"Unfucking nested links in {filepath}")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    unfuck_links()
