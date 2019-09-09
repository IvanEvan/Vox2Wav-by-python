#### This is a way to convert audio vox file (Dialogic ADPCM) to wav file (PCM) via python.
#### You can use the .exe file to do the conversion from the command line.(better effect)
#### Or use Python implementation of the Dialogic ADPCM algorithm.(more convenient)

---
- Cause                
Vox files are widely used in telephone recording system. I need deal with them by python. But seems python just has interface for PCM encoding format audio, vox's encoding format is Dialogic ADPCM.      

---

- Two solutions come to mind:        
1. read data from vox file directly       
2. convert vox to PCM file        

---

- I found some C++, C# and java code for above work, but not python.       

---
**Usage for exe file**         

&emsp;1. copy 'use-exe-tool/vox_2_wav.py' and 'use-exe-tool/Vox2Pcm.exe' to your folder     

&emsp;2. run vox_2_wav.py      
                  
**Usage for python**    

&emsp;1. run 'use-python/dialogic_ADPCM.py'            

---
- Performance         
![image](http://note.youdao.com/noteshare?id=ea99c70e6811103eccd7e6431e69d214&sub=15F57180671D4CC1844E6AAF04C13489)           
The upper part is the result of .exe.           
And the lower part is the result of python code.      
They're not very different.        
The top one looks better.        
But the one down there can keep data in the RAM not use HDD, Time-consuming IO are avoided.

---
- Appendix    
                  
&emsp;1. Thanks to the [zhanzr](https://github.com/zhanzr) !!!! I found his [blog](http://www.21ic.com/evm/audiolist/201706/724814.htm) about IMA ADPCM, which similar to Dialogic ADPCM. And he posted Python implementation. I got in touch with him, and he gave me some ideas. Follow his [instructions](https://wiki.multimedia.cx/index.php/Dialogic_IMA_ADPCM), I changed his code to Dialogic ADPCM.
                    
&emsp;2. Vox2Pcm.exe was provided by the "BlueSpace Co" open source. You can got other transfor tools in [here](http://www.bluespace.com.cn/koodoo/download_wav2a.html). Thanks this company!!!
                 
&emsp;3. vcecopy.exe was provided by the "Dialogic Co" and documents is [here](https://www.dialogic.com/support/logon.aspx?nextpage=/support/helpweb/helpweb.aspx/3395/supported_sampling_rates_for_input_audio_files_for_vcecopy/). I cound't find how to install it but I found a [offline-way](https://wiki.freepbx.org/plugins/servlet/mobile?contentld=95358484#HowtorunvcecopywithoutafullNaturalAccessinstallation-Introduction) to use it.And it seems like many .dll files to dependent.     
             
&emsp;4. You also can use command "sox" to do convert. For me,it worked. I can implement vox file to wav file by use sox. But, the wav file's time domain waveform deviant. The center of the signal deviates from the zero axis as a whole. ~~I can't fixed.~~ Because the original Dialogic ADPCM algorithm is decode 4bit to 12bit, not 16bit. The "sox" use the default version.        
              
&emsp;5. I also found some other [blog](http://lhari.hu/transcoding-in-freeswitch-from-dialogic-adpcm-to-g711/) or [issue](https://sourceforge.net/p/sox/bugs/274/) about Dialogic ADPCM. They are also very useful!

