[app]
title = انبار دار
package.name = anbardar
package.domain = org.mystore
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,db
source.exclude_dirs = .buildozer, bin
version = 1.0.0
requirements = python3,kivy,android,sqlite3
orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.accept_sdk_license = True

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 0
