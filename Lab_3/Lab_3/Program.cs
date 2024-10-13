using System;

class Program
{
    // Функція корисності
    static double Utility(double x)
    {
        return 0.1 * x * x;
    }

    // Сподіваний виграш лотереї
    static double ExpectedValue(double[] probabilities, double[] outcomes)
    {
        double expectedValue = 0;
        for (int i = 0; i < probabilities.Length; i++)
        {
            expectedValue += probabilities[i] * outcomes[i];
        }
        return expectedValue;
    }

    // Сподівана корисність лотереї
    static double ExpectedUtility(double[] probabilities, double[] outcomes)
    {
        double expectedUtility = 0;
        for (int i = 0; i < probabilities.Length; i++)
        {
            expectedUtility += probabilities[i] * Utility(outcomes[i]);
        }
        return expectedUtility;
    }

    // Детермінований еквівалент
    static double CertaintyEquivalent(double expectedUtility)
    {
        return Math.Sqrt(expectedUtility / 0.1);
    }

    // Премія за ризик
    static double RiskPremium(double expectedValue, double certaintyEquivalent)
    {
        return expectedValue - certaintyEquivalent;
    }

    static void Main()
    {
        // Лотерея 1: L1(0; 0.5; 20)
        double[] probabilities_L1 = { 0.5, 0.5 };
        double[] outcomes_L1 = { 0, 20 };

        // Лотерея 2: L2(10; 0.5; 30)
        double[] probabilities_L2 = { 0.5, 0.5 };
        double[] outcomes_L2 = { 10, 30 };

        // Сподіваний виграш
        double ev_L1 = ExpectedValue(probabilities_L1, outcomes_L1);
        double ev_L2 = ExpectedValue(probabilities_L2, outcomes_L2);

        // Сподівана корисність
        double eu_L1 = ExpectedUtility(probabilities_L1, outcomes_L1);
        double eu_L2 = ExpectedUtility(probabilities_L2, outcomes_L2);

        // Детермінований еквівалент
        double ce_L1 = CertaintyEquivalent(eu_L1);
        double ce_L2 = CertaintyEquivalent(eu_L2);

        // Премія за ризик
        double rp_L1 = RiskPremium(ev_L1, ce_L1);
        double rp_L2 = RiskPremium(ev_L2, ce_L2);

        // Виведення результатів
        Console.WriteLine("Лотерея L1:");
        Console.WriteLine($"Сподiваний виграш: {ev_L1:F2}");
        Console.WriteLine($"Сподiвана кориснiсть: {eu_L1:F2}");
        Console.WriteLine($"Детермiнований еквiвалент: {ce_L1:F2}");
        Console.WriteLine($"Премiя за ризик: {rp_L1:F2}");
        Console.WriteLine();

        Console.WriteLine("Лотерея L2:");
        Console.WriteLine($"Сподiваний виграш: {ev_L2:F2}");
        Console.WriteLine($"Сподiвана кориснiсть: {eu_L2:F2}");
        Console.WriteLine($"Детермiнований еквiвалент: {ce_L2:F2}");
        Console.WriteLine($"Премiя за ризик: {rp_L2:F2}");
        Console.WriteLine();

        // Вибір лотереї
        if (ce_L1 > ce_L2)
        {
            Console.WriteLine("Особа обере лотерею L1.");
        }
        else if (ce_L2 > ce_L1)
        {
            Console.WriteLine("Особа обере лотерею L2.");
        }
        else
        {
            Console.WriteLine("Особа байдужа до вибору мiж лотереями.");
        }

        // Оцінка схильності до ризику
        if (rp_L1 > 0 && rp_L2 > 0)
        {
            Console.WriteLine("Особа не схильна до ризику.");
        }
        else
        {
            Console.WriteLine("Особа схильна до ризику.");
        }
    }
}