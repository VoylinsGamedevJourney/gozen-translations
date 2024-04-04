import os


def generate_mo_files():
    print('-= Generating *.mo files =-')
    print('Updating git ...')
    os.system('git pull')

    current_dir = os.path.dirname(__file__)
    po_files_dir = os.path.join(current_dir, 'po_files')

    os.chdir(po_files_dir) # Change directory to po_files

    for po_file in os.listdir('.'):
        if po_file.endswith('.po'):
            mo_file = os.path.join(current_dir, '../src/translations/', po_file[:-3] + '.mo')
            os.system(f'msgfmt -o {mo_file} {po_file}')

            print(f'Generated: {po_file[:-3]}.mo')

    os.chdir(current_dir) # Go back to the original directory
    print('-= Generating localization files complete! =-')


if __name__ == '__main__':
    generate_mo_files()
