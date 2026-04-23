import os
import subprocess
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("=" * 50)
        print(" " * 15 + "YT-DLP Easy CLI")
        print("=" * 50)
        
        url = input("\n1. Enter the YouTube link to download: ").strip()
        if not url:
            print("Error: URL cannot be empty.")
            input("Press Enter to continue...")
            continue

        print("\n2. What do you want to download?")
        print("   [1] Video (MKV)")
        print("   [2] Audio Only (MP3)")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()

        if choice == '1':
            print("\nSelect Video Quality:")
            print("   [1] 720p")
            print("   [2] 1080p")
            print("   [3] 2K (1440p)")
            print("   [4] 4K (2160p)")
            print("   [5] Best Quality Available")
            
            v_choice = input("\nEnter your choice (1-5): ").strip()
            
            quality_map = {
                '1': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
                '2': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
                '3': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',
                '4': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
                '5': 'bestvideo+bestaudio/best'
            }
            
            format_str = quality_map.get(v_choice, 'bestvideo+bestaudio/best')
            
            print("\nStarting download...")
            command = [
                'yt-dlp',
                '-f', format_str,
                '--merge-output-format', 'mkv',
                url
            ]
            
        elif choice == '2':
            print("\nSelect Audio Quality:")
            print("   [1] 128 kbps")
            print("   [2] 192 kbps")
            print("   [3] 256 kbps")
            print("   [4] 320 kbps")
            print("   [5] Best Audio")
            
            a_choice = input("\nEnter your choice (1-5): ").strip()
            
            quality_map = {
                '1': '128',
                '2': '192',
                '3': '256',
                '4': '320',
                '5': '0'
            }
            
            audio_quality = quality_map.get(a_choice, '0')
            
            print("\nStarting download...")
            command = [
                'yt-dlp',
                '-f', 'bestaudio',
                '--extract-audio',
                '--audio-format', 'mp3'
            ]
            if audio_quality != '0':
                command.extend(['--audio-quality', f'{audio_quality}K'])
            else:
                command.extend(['--audio-quality', '0'])
            
            command.append(url)
            
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")
            continue

        try:
            subprocess.run(command)
            print("\nDownload finished successfully!")
        except FileNotFoundError:
            print("\nError: 'yt-dlp' was not found on your system.")
            print("Please ensure it is installed and added to your system PATH.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            
        again = input("\nDo you want to download another file? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
