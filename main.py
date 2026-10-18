import os
import threading
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform

class AnbardarApp(App):
    def build(self):
        self.title = "انبار دار"
        os.environ["ANBAR_DATA_DIR"] = self.user_data_dir
        
        from server_app import main as run_server_main
        self.run_server_main = run_server_main
        
        Clock.schedule_once(self.start_server, 0.5)
        return Label(text="در حال راه‌اندازی انبار دار...\nلطفاً صبر کنید.")

    def start_server(self, dt):
        def server_thread():
            try:
                self.run_server_main()
            except Exception as e:
                print("Server error:", e)
                
        t = threading.Thread(target=server_thread)
        t.daemon = True
        t.start()
        
        time.sleep(2)
        
        if platform == 'android':
            try:
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                Uri = autoclass('android.net.Uri')
                intent = Intent(Intent.ACTION_VIEW)
                intent.setData(Uri.parse("http://127.0.0.1:8765"))
                PythonActivity.mActivity.startActivity(intent)
            except Exception as e:
                print("Error opening browser:", e)
        else:
            import webbrowser
            webbrowser.open("http://127.0.0.1:8765")

    def on_pause(self):
        return True

if __name__ == "__main__":
    AnbardarApp().run()
