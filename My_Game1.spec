# -*- mode: python -*-

block_cipher = None


a = Analysis(['My_Game1.py'],
             pathex=['C:\\Users\\sukoc\\Desktop\\Artemiy\\My game\\dist'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='My_Game1',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
