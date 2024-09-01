alias record='function _record() {
     local display=$(echo $DISPLAY)
    local screen="0"
    local fps=60
    local output_dir="$HOME/Recordings"
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local extra_opts=""
    local audio_opts=""
    local custom_output=""

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --s1) screen="0" ;;
            --s2) screen="1" ;;
            --fps)
                fps="$2"
                shift
                ;;
            --nvenc)
                extra_opts="-c:v h264_nvenc -preset llhq -rc vbr_hq -cq 19 -b:v 30M -maxrate:v 60M"
                ;;
            --audio)
                audio_opts="-f pulse -ac 2 -i default"
                ;;
            --output)
                custom_output="$2"
                shift
                ;;
            *)
                echo "Unknown option: $1"
                return 1
                ;;
        esac
        shift
    done

    if [ -z "$custom_output" ]; then
        custom_output="$output_dir/screen_${screen}_${timestamp}.mp4"
    fi

    local video_opts="-f x11grab -s 2560x1440 -r $fps -i $display.$screen"
    local encode_opts="${extra_opts:--c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p} -c:a aac"

    local command="ffmpeg $video_opts $audio_opts $encode_opts $custom_output"

    echo "Executing: $command"
    eval "$command"
}; _record'
