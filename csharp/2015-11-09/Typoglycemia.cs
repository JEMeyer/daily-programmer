using System;
using System.Text;
using System.Linq;

class Typoglycemia
{
    static void Main(string[] args)
    {
        // Get the input phrase, seperated by words
        Console.WriteLine("Please enter input phrase:");
        string[] input = Console.ReadLine().Split(' ');
        
        // Call scramble on each word
        for (int i = 0; i < input.Length; i++)
        {
            // Don't scramble if it's length 1 - 3
            if (input[i].Length > 3) {
                input[i] = scramble(input[i]);
            }
        }
        
        // Print out the new phrase
        input.ToList().ForEach (i => Console.Write(i.ToString() + ' '));
        Console.WriteLine();
    }
    
    // Takes in a string, returns a 'scrambled' version of that string,
    // with the first and last letters in same place, but internal letters
    // will be in random indexes
    static string scramble(string input)
    {   
        // Non-random, but 4 letter words should have position 2 and 3 switched
        // to make them look scrambled. Pure luck means it might be the same
        if (input.Length == 4)
        {
            char[] word = input.ToCharArray();
            char temp = word[2];
            word[2] = word[3];
            word[3] = temp;
            return new string(word);
        }
        
        // Get each letter, create StringBuilder, save off length
        char[] letters = input.ToCharArray();
        StringBuilder output = new StringBuilder();
        int phraseLength = letters.Length;
        
        // Store off first and last letter, and mark them 'taken care of'
        output.Append(letters[0]);
        letters[0] = '`';
        char lastLetter = letters[phraseLength-1];
        letters[phraseLength-1] = '`';
        
        Random rnd = new Random(10);   
     
        // Keep scrambling until every letter in the word is accounted for
        while (true)
        {
            int index = rnd.Next(1, phraseLength-1);
            if (letters[index] == '`')
            {
                continue;
            }
            output.Append(letters[index]);
            letters[index] = '`';
            // ` is my placeholder for 'taken care of'
            if (letters.All(x => x == '`'))
            {
                break;   
            }
        }
        
        // Tack on the last character and return the new word
        output.Append(lastLetter);
        return output.ToString();
    }
}