filewrap

A Python module that wraps functionality from the os module for file system manipulation and management.

Make sure to have the latest version of Python 3 installed although this should work with previous versions. 
Pip and git also need to be installed for module installation with command line.  

To install/update the module with pip enter command in terminal:
    pip install git+https://github.com/CodeConfidant/filewrap-os.git#egg=filewrap-os

To uninstall the module with pip enter command in terminal:
    pip uninstall filewrap

Method 	                                Description
copydir(destination_path, target_path) 	Copy target directory and all of it's subdirectories/files to a destination directory.

copyfile(destination_path, *filepaths) 	Copy single/multiple files to destination directory.
                                        The destination_path and *filepaths arguments must be strings.

rpfile(mode, *filepaths) 	            Read and print lines in single/multiple text/binary based files.
                                        The mode argument must be either strings: "t" (text) or "b" (binary).
                                        The *filepaths arguments must be strings.

rmfile(*filepaths) 	                    Delete single/multiple files.
                                        The *filepaths arguments must be strings.

mkfile(mode, *filepaths) 	            Make single/multiple text/binary based files.
                                        The mode argument must be either strings: "t" (text) or "b" (binary).
                                        The *filepaths arguments must be strings.

rmdir(*filepaths)                   	Delete single/multiple directories.
                                        The *filepaths arguments must be strings.

rmall(dirpath) 	                        Delete single directory along with it's subdirectories and files.
                                        Use this with caution, as you could delete your entire file system if you're not careful.

mkdir(*filepaths) 	                    Make single/multiple directories.
                                        The *filepaths arguments must be strings.

rpdir(*filepaths)	                    Output to terminal the file/subdirectory names of single/multiple argument filepaths. 
                                        Use no arguments for working directory only. 
                                        The *filepaths arguments must be strings.

lsdir(*filepaths)	                    Return a list with file/subdirectory names of the single/multiple argument filepaths. 
                                        If there are no arguments used in *filepaths, a list of the contents within the working directory is returned. 
                                        If there is only one argument used in *filepaths, a list of the contents of only that filepath directory is returned. 
                                        Using the method with two or more arguments in *filepaths will return a list of lists with each list containing the file/subdirectory names of that filepath argument.

chdir(filepath) 	                    Change current working directory.
                                        The filepath argument must be a string.

wdir() 	                                Return string of the path of the current working directory.

pwdir() 	                            Print working directory to terminal.

mklist(mode, *filepaths) 	            Return a list from lines in single/multiple text/binary based files.
                                        The mode argument must be either strings: "t" (text) or "b" (binary).
                                        The *filepaths arguments must be strings.

writelines(mode, filepath, *lines) 	    Write singular strings or lists of elements in sequence to lines in a text/binary based file.
                                        The mode argument must be either strings: "t" (text) or "b" (binary).
                                        The filepath argument must be a string.
                                        The lines in the file are overwritten by the lines argument values.

appendlines(mode, filepath, *lines) 	Append singular strings or lists of elements in sequence to lines at the end of a text/binary based file.
                                        The mode argument must be either strings: "t" (text) or "b" (binary).
                                        The filepath argument must be a string.

attrfile(mode, filepath) 	            Return information about a file as dictionary.
                                        The mode argument value can be one of the following strings: "rt", "at", "wt", "rb", "ab", "wb"
                                        The filepath argument must be a string.

path_exists(filepath) 	                Return boolean value (True or False) to check if a single file path exists.
                                        The filepath argument must be a string.

isfile(filepath) 	                    Return boolean value (True or False) to check if filepath argument is a file.
                                        The filepath argument must be a string.

isdir(filepath) 	                    Return boolean value (True or False) to check if filepath argument is a directory.
                                        The filepath argument must be a string.

ren(current_filepath, desired_filepath) Rename single/multiple files or directories.
                                        current_filepath represents the file path's name being changed.
                                        desired_filepath represents the file path's new intended name.
                                        current_filepath and desired_filepath can either be:
                                            Two strings
                                            Two lists of equal length consisting of strings