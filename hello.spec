# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['hello.py'],
             pathex=['.'],
             binaries=[
                ('./src/gateway/gateway.cpython-311-x86_64-linux-gnu.so', 'src/gateway'),
                ('./src/logic/super_secret_library.cpython-311-x86_64-linux-gnu.so', 'src/logic')
             ],
             datas=[],
             hiddenimports=["fastapi"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='hello',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )