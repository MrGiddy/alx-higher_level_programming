#!/usr/bin/node
/*
 * Concats two files
 * First arg, argv[2]: first source file
 * Second arg, argv[3]: second source file
 * Third arg, argv[4]: destination file
 *
 */

/* Import fs module */
const fs = require('node:fs');

const file1 = fs.readFileSync(process.argv[2], 'utf8');
const file2 = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], file1 + file2);
