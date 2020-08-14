'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    vocales(s);
    consonantes(s);
}

function vocales(input) {
    var v = 'aeiou';
    var splitted = v.split('');
    var op = input.split('').filter(function(item) {
        if (v.includes(item)) {
            console.log(item);
        }
    });
}

function consonantes(input) {
    var v = 'bcdfghjklmnpqrstvwxyz';
    var splitted = v.split('');
    var op = input.split('').filter(function(item) {
        if (v.includes(item)) {
            console.log(item);
        }
    });
}