"""
Helper Script For Building Executable
"""
import subprocess, os, shutil,sys
if __name__ == '__main__':




    # Establish Paths
    script_path = os.path.join(os.path.dirname(__file__),'main.py')
    dist_path = os.path.dirname(__file__)
    spec_path = os.path.join(os.path.dirname(__file__),'main.spec')
    icon_path = os.path.join(os.path.dirname(__file__),'Images/logo.ico')

    # Make Sure Destination build dir is wiped clean
    try:
        shutil.rmtree(os.path.join(dist_path,'build'))
        shutil.rmtree(os.path.join(dist_path,'main'))
    except WindowsError:
        pass




    subprocess.call(['python', '--version'])
    subprocess.call(['python', script_path])


    # Make Spec File

    sys_paths = ['--paths=%s'%path for path in sys.path]
    spec_arg_list = ['pyi-makespec']
    spec_arg_list.extend(sys_paths)
    spec_arg_list.append(script_path)
    spec_arg_list.append('--onefile')
    print('\nSubprocess Call: %s' % ' '.join(spec_arg_list))
    subprocess.call(spec_arg_list)


    # Start New Build
    arg_list = ['pyinstaller',script_path,
                '--onefile',
                '--windowed',
                # '--distpath',dist_path,
                '--icon=%s'%icon_path,
                ]
    print('\nSubprocess Call: %s'%' '.join(arg_list))
    subprocess.call(arg_list)
