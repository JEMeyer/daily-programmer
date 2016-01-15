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
        
        for (int i = 0; i < input.Length; i++)
        {
            input[i] = scramble(input[i]);
        }
        
        input.ToList().ForEach (i => Console.Write(i.ToString() + ' '));
        Console.WriteLine();
    }
    
    // Takes in a string, returns a 'scrambled' version of that string,
    // with the first and last letters in same place, but internal letters
    // will be in random indexes
    static string scramble(string input)
    {
        if (input.Length == 1 || input.Length == 2 || input.Length == 3)
        {
            return input;
        }
        char[] letters = input.ToCharArray();
        StringBuilder output = new StringBuilder();
        int phraseLength = letters.Length;
        output.Append(letters[0]);
        letters[0] = '`';
        char lastLetter = letters[phraseLength-1];
        letters[phraseLength-1] = '`';
        
        Random rnd = new Random(10);   
     
        while (true)
        {
            int index = rnd.Next(1, phraseLength-1);
            if (letters[index] == '`')
            {
                continue;
            }
            output.Append(letters[index]);
            letters[index] = '`';
            if (letters.All(x => x == '`'))
            {
                break;   
            }
        }
        output.Append(lastLetter);
        return output.ToString();
    }
}