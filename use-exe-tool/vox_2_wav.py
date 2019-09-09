#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 14:52
# @Author  : Evan
# @File    : vox_2_wav.py
import os
import sys
import time
import shutil
import subprocess

EXE_TOOL = 'Vox2Pcm'


def vox_convert_wav(vox_file, transf_tool, out_path):
    st = time.time()

    os_name = sys.platform

    vox_folder, vox_name = os.path.split(vox_file)  # return vox file folder and vox file name

    shutil.copy(vox_file, vox_name)  # copy target vox file to this folder

    if os_name.startswith('win'):
        command = [transf_tool, vox_name]
    else:
        command = ['wine', transf_tool, vox_name]  # linux use command wine to run  .exe

    _ = subprocess.check_output(command, shell=True)  # run convert command

    os.remove(vox_name)  # remove the copied vox file

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    wav_name = str(vox_name.split('.vox')[0]) + '.wav'

    shutil.move(wav_name, os.path.join(out_path, wav_name))  # move the generated wav file

    et = time.time()
    return et - st


if __name__ == '__main__':
    vox_file = r'E:\vox\xxx.vox'
    # vox file needs the same level folder with Vox2Pcm.exe
    tm = vox_convert_wav(vox_file, EXE_TOOL, r'D:\wave')
    print(f"Convert '{vox_file}' use {tm} s")
