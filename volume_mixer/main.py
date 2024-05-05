from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

VOLUME = 0.04  # [0.0, 1.0]


def main() -> None:
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if not session.Process or session.Process.name() != "Discord.exe":
            continue
        for pmmap in session.Process.memory_maps():
            if "notification" in pmmap.path:
                break
        else:
            # Discordの通知音に対応したミキサーをいじる
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            bef = volume.GetMasterVolume()
            volume.SetMasterVolume(VOLUME, None)
            print(f"Change discord notification volume from {bef} to {VOLUME}")


if __name__ == "__main__":
    main()
