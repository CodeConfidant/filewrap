# ***filewrap***

    Python package for file/directory/archive management.

    Python version 3.6 is required at a minimum. 

    To install/update the package with pip enter command in terminal:
        pip install filewrap

    To uninstall the package with pip enter command in terminal:
        pip uninstall filewrap

    Built-in modules used: os, tarfile, zipfile

<table width='100%'>
	<tr>
		<th align='left'>
            Method
        </th>
		<th align='left'>
            Description
        </th>
	</tr>
    <tr>
		<td>
            <code>copydir(destination_path, target_path)</code>
        </td>
		<td>
            Copy target directory and all of it's subdirectories/files to a destination directory.
        </td>
	</tr>
    <tr>
		<td>
            <code>copyfile(destination_path, *filepaths)</code>
        </td>
		<td>
            Copy single/multiple files to destination directory. <br/>
            The destination_path and *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>read(filepath)</code>
        </td>
		<td>
            Read the binary from a file and return. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>write(data, filepath)</code>
        </td>
		<td>
            Write bytes object to a file. <br/>
            The filepath argument must be a string. <br/>
            The data argument must be a bytes object.
        </td>
	</tr>
	<tr>
		<td>
            <code>rpfile(mode, *filepaths)</code>
        </td>
		<td>
            Read and print lines in single/multiple text/binary based files. <br/>
            The mode argument must be either strings: 't' (text) or 'b' (binary). <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>rmfile(*filepaths)</code>
        </td>
		<td>
            Delete single/multiple files. <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>mkfile(mode, *filepaths)</code>
        </td>
		<td>
            Make single/multiple text/binary based files. <br/>
            The mode argument must be either strings: 't' (text) or 'b' (binary). <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>rmdir(*filepaths)</code>
        </td>
		<td>
            Delete single/multiple directories. <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>rmall(dirpath)</code>
        </td>
		<td>
            Delete single directory along with it's subdirectories and files. <br/>
            Use this with caution, as you could delete your entire file system if you're not careful.
        </td>
	</tr>
    <tr>
		<td>
            <code>mkdir(*filepaths)</code>
        </td>
		<td>
            Make single/multiple directories. <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>rpdir(*filepaths)</code>
        </td>
		<td>
            Output to terminal the file/subdirectory names of single/multiple argument filepaths. <br/>
            Use no arguments for working directory only. <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>lsdir(filepath)</code>
        </td>
		<td>
            Return a list with file/subdirectory names of the single argument directory.
            If there is no argument used in filepath, a list of the contents (e.g. paths of files & directories) within the working directory is returned.
            If there is one argument used in filepath, a list of the contents of only that directory is returned.
        </td>
	</tr>
    <tr>
		<td>
            <code>chdir(filepath)</code>
        </td>
		<td>
            Change current working directory. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>wdir()</code>
        </td>
		<td>
            Return string of the path of the current working directory.
        </td>
	</tr>
    <tr>
		<td>
            <code>pwdir()</code>
        </td>
		<td>
            Print working directory to terminal.
        </td>
	</tr>
    <tr>
		<td>
            <code>mklist(*filepaths)</code>
        </td>
		<td>
            Return a list from lines in single/multiple text based files. <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>writelines(filepath, *lines)</code>
        </td>
		<td>
            Write singular strings or lists of strings in sequence to lines in a text based file. <br/>
            The filepath argument must be a string. <br/>
            The lines in the file are overwritten by the lines argument values.
        </td>
	</tr>
    <tr>
		<td>
            <code>appendlines(filepath, *lines)</code>
        </td>
		<td>
            Append singular strings or lists of strings in sequence to lines at the end of a text based file. <br/> 
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>path_exists(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if a single file path exists. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>isfile(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if filepath argument is a file. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>isdir(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if filepath argument is a directory. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>istar(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if filepath argument is a tar archive. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>iszip(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if filepath argument is a zip archive. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>ren(current_filepath, desired_filepath)</code>
        </td>
		<td>
            Rename single/multiple files or directories. <br/>
            current_filepath represents the file path's name being changed. <br/>
            desired_filepath represents the file path's new intended name. <br/>
            current_filepath and desired_filepath can either be:
            <ul>
                <li>Two strings</li>
                <li>Two lists of equal length consisting of strings</li>
            </ul>
        </td>
	</tr>
    <tr>
		<td>
            <code>tar_wrap(filepath)</code>
        </td>
		<td>
            Create a tar archive with gzip compression & .gz extension.
        </td>
	</tr>
    <tr>
		<td>
            <code>tar_extract(filepath)</code>
        </td>
		<td>
            Extract a tar gzip archive contents to working directory.
        </td>
	</tr>
     <tr>
		<td>
            <code>zip_wrap(filepath)</code>
        </td>
		<td>
            Create a zip archive with DEFLATE compression.
        </td>
	</tr>
    <tr>
		<td>
            <code>zip_extract(filepath)</code>
        </td>
		<td>
            Extract a zip archive contents to working directory.
        </td>
	</tr>
    <tr>
		<td>
            <code>filecount(filepath)</code>
        </td>
		<td>
            Count and return the number of files within a directory.
        </td>
	</tr>
    <tr>
		<td>
            <code>dircount(filepath)</code>
        </td>
		<td>
            Count and return the number of directories within a directory.
        </td>
	</tr>
    <tr>
		<td>
            <code>size(*filepaths)</code>
        </td>
		<td>
            Get the total combined size in bytes of the file paths & directories within the *filepaths argument.
        </td>
	</tr>
</table>

[Back to Top](#filewrap)

---
