const fs = require('fs');

// Get file paths from command line arguments
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

// Read contents of source files
fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  if (err1) throw err1;

  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    if (err2) throw err2;

    // Concatenate contents of both files
    const concatenatedData = data1 + data2;

    // Write concatenated data to the destination file
    fs.writeFile(destinationFile, concatenatedData, err => {
      if (err) throw err;
      console.log('Files concatenated successfully!');
    });
  });
});
