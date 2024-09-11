#!/usr/bin/osascript
tell application "Terminal"
    activate
    do script ". /Users/cyh/opt/anaconda3/bin/activate && conda activate /Users/cyh/opt/anaconda3/envs/webscrap; python -i"
end tell
