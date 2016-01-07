using System;

class RecurrenceRelation
{
    static void Main(string[] args)
    {
        // Get equation, starting number, and iteration count
        Console.WriteLine("Please enter tranformation equation:");
        string[] transformation = Console.ReadLine().Split(' ');
        Console.WriteLine("Enter starting term:");
        int startingTerm = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Ender number of iterations:");
        int iterations = Convert.ToInt32(Console.ReadLine());

        // List first iteration and then call recursive function
        Console.WriteLine("Term 0: " + startingTerm);
        recurse(transformation, startingTerm, iterations, 0);
    }

    static void recurse(string[] transform, int term, int count, int termNum)
    {
        // We are done
        if (termNum == count)
        { return; }

        // Loop for each part of transformation equation
        for (int i = 0; i < transform.Length; i++)
        {
            // Get operator and value
            string op = transform[i].Substring(0, 1);
            int val = Convert.ToInt32(transform[i].Substring(1));

            // Calculate
            switch (op)
            {
                case "+":
                    term += val;
                    break;
                case "-":
                    term -= val;
                    break;
                case "*":
                    term *= val;
                    break;
                case "/":
                    term /= val;
                    break;
            }
        }

        // Output
        Console.WriteLine(string.Format("Term {0}: {1}", ++termNum, term));

        // Call self
        recurse(transform, term, count, termNum);
    }
}
