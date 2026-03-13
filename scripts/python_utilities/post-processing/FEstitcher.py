import os
import time
import shutil
import json
import  re

class Stitcher:
    def __init__(self):
        # Keeps track of which binary files have already been "staged"/handled/
        # converted
        self.files_staged = []
        self.retrieve_information()



    def retrieve_information(self):
        """

            Retrieve the values for the location of the FastEddy binary files, the
            filename format for the binary files, the location of the
            staging directory (where files are to be copied and worked on),
            and the time for sleep (in seconds).

            All this information is saved in a named tuple.

            Args:
                None, retrieves values from the environment variables set in the BASH
                script used to invoke the FastEddy simulation.

            Returns:
               None, sets class variables

        """

        # Set up the named tuple

        # Retrieve the location of the binary files from the convert.json file
        convert_src_dir = os.getenv('CONVERTSRCDIR')

        # read the convert.json file and retrieve the value of "outputpath"- the
        # location of the FastEddy binary files
        convert_json_file = os.path.join(convert_src_dir, 'convert.json')
        with open(convert_json_file) as file:
            params = json.loads(file.read())
        self.fe_bin_dir = params["outpath"]

        # Retrieve the filename format
        self.bin_file_format = os.getenv('BINARYFILEPREFIX')

        # Retrieve the number of seconds for sleep
        self.sleep_secs = os.getenv('SLEEPSECS')

        # Retrieve the location of the staging directory
        self.staging_dir = os.getenv('STAGINGDIR')


    def copy_binaries(self) -> None:
        """
           Copies FastEddy binary files to a target directory where stitching can take place
           using the FEbinaryToNetCDF module

            Args:
               destination: Directory where binary files are to be copied
           Returns:
               None
        """
        print("Inside copy_binaries()")
        # Check directory for binary files that have expected file name format
        all_files = os.listdir(self.fe_bin_dir)
        for cur in all_files:
            if cur not in self.files_staged:
                pattern = re.compile(self.bin_file_format)
                match = re.match(pattern, cur)
                if match:
                    self.files_staged.append(cur)
                    self.process_binary(cur)




    def process_binary(self, bin_file):
        """
            Invokes the FEbinaryToNetCDF.py module to perform the conversion of the
            binary files to NetCDF.

        Returns:
            None

        """

        # Copy the binary files to a staging directory, only copy files that haven't
        # already been copied
        print(f"invoke FEbinaryToNetCDF for file {bin_file} after modifying the corresponding convert.json file")
        print("Copying to staging directory")
        origin = os.path.join(self.fe_bin_dir, bin_file)
        destination = os.path.join(self.staging_dir, bin_file)
        os.makedirs(self.staging_dir, exist_ok=True)
        shutil.copy(origin, destination)

        # ToDo invoke the FEbinaryToNetCDF module here


if __name__ == "__main__":
    print("inside FEstitcher")

    stitcher = Stitcher()

    for i in range(2):
       print(f"Sleeping for {stitcher.sleep_secs} secs")
       time.sleep(int(stitcher.sleep_secs))
       print('Waking up, time to do something.')
       # Perform action(s)
       stitcher.copy_binaries()
