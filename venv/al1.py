import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] =100


def CALC(d):
    X = []
    Y = []

    for deltaf in range(1, 1000, 1):
        deltaf = deltaf / 1000
        # Parametry procesowe z zalozen: 30 W/cm^2, epsilonI/epsilonII = 1/2, tgdeltaI/tgdeltaII = 1/5 , f = 27.12 MHz
        S = 10  # Powieszchnia elektrody <cm^2>
        d = 0.1  # Grubosc wsadu (2 warstwy) <cm>
        f = 27.12  # Czestotliwosc zgrzewania <MHz>
        #    deltaf = 0.163 # Szerokosc pasma <MHz>
        epsilonI = 6  # stała dielektryczna na poczatku zgrzewania
        epsilonII = 12  # stala dielektryczna na koncu zgrzewania
        tgdeltaI = 0.1  # Stratnosc dielektryczna na poczatku procesu zgrzewania
        tgdeltaII = 0.5  # Stratnosc dielektryczna na koncu procesu zgrzewania
        thetaIIo = 0.8  # Sprawnosc obwodu
        # -------------------------------------------------------------------------------------------------------------

        # Temperatura 20C
        CIf = 0.0886 * epsilonI * S / d  # Pojemnosc zgrzewanej folii na poczatku zgrzewania <pF>
        BIf = f * CIf / 159  # Susceptancja rownolegla na poczatku zgrzewania <mS>
        GIf = BIf * tgdeltaI  # Konduktancja rownolegla na poczatku zgrzewania <mS>

        # Temperatura 150C
        BIIf = BIf * epsilonII / epsilonI  # Susceptancja rownolegla na koncu zgrzewania <mS>
        GIIf = BIIf * tgdeltaII  # Konduktancja rownolegla na koncuu zgrzewania <mS>

        Puzmin = S * 30  # Wartosc ponizej ktorej nie moze spadac  -> kryterium 30 W/cm^2
        #    print('Minimalna wartosc mocy w trakcie zgrzewania Puzmin =', Puzmin, 'W')
        Pa1 = 3.8 * Puzmin  # Minimalna moc wyjscowa triody dla poczatku procesu zgrzewania
        #    print('Moc wyjsciowa triody musi wynosic co najmniej', Pa1, 'W')

        # Parametry wybranej triody prozniowej T380-1
        Ua1 = 3600  # Napiecie WCz na anodzie <V>
        Us1 = 470  # Napiecie wzbudzenia siatki <V>
        Is0 = 0.072  # Prad polarizacji siatki <A>
        Is1 = 2 * Is0  # Przyblizona wartosc pradu wzbudzenia siatki <A>
        Rs = 4300  # Rezystancja gridleaka <Ohm>
        #    print('Rezystancja gridleaka Rs =', Rs, 'Ohm')
        Csk = 7.5  # Pojemnosc pomiedzy siatka a katoda w wybranej triodzie <pF>
        Pwzb = Us1 * Is1 / 2  # Moc wzbudzenia siatki <W>
        Rd = Ua1 * 0.95 / (2 * Puzmin)  # Rezystancja obciazenia <kOhm>
        # --------------------------------------------------------------------------------------------------------------

        # Obliczenie reszty parametrow
        Ps = Us1 ** 2 / (2 * Rs)  # Moc tracona w oporniku siatkowym
        PIwzb = Pwzb + Ps  # Moc dostarczona do obwodu siatki
        RIwzb = Us1 ** 2 / (2 * PIwzb)  # Rezystancja obciazajaca obwod sprzezenia zwrotnego
        m = Us1 / Ua1  # Wspolczynnik sprzezenia zwrotnego
        Xas = RIwzb * math.tan(10 * np.pi / 180) / (1 + m)  # Maksymalna reaktancja miedzy siatka a katoda
        #    print('Maksymalna reaktancja miedzy siatka a katoda', Xas, 'Ohm')
        Cs = 10 * Csk  # Minimalna pojemnosc sprzegajaca obwod siatki <pF>
        #    print('Minimalna pojemnosc sprzegajaca obwod siatki Cs =', Cs, 'pF')
        PIa1 = Pa1 - PIwzb  # Moc dostarczana przez lampe do obwody wyjsciowego
        #    print('Moc dostarczana przez lampe do obwody wyjsciowego', PIa1, 'W')
        RId = Ua1 ** 2 / (2 * PIa1)  # Rezystancja rownolegla odpowiadajaca mocy dostarczonej do obwodu wyjsciowego
        # -------------------------------------------------------------------------------------------------------------

        # Obliczenie linii transmisji mocy
        Z0 = 70  # opor falowy linii koncentrycznej, przy czym impedancja obciazenia ZA = Z0^2*Yf
        #    print('Impedancja linii transmisyjnej Z0 =', Z0, 'Ohm')
        ZIA = Z0 ** 2 * complex(GIf / 1000,
                                BIf / 1000)  # Impedancja linii transmisijnej podlaczonej do pracy na poczatku zgrzewania. /1000 dlatego ze wartosci zrodlowe sa w <mS>
        ZIIA = Z0 ** 2 * complex(GIIf / 1000,
                                 BIIf / 1000)  # Impedancja linii transmisijnej podlaczonej do pracy na koncu zgrzewania. /1000 dlatego ze wartosci zrodlowe sa w <mS>
        # -------------------------------------------------------------------------------------------------------------

        # Oszacowanie dryftu
        dryft = deltaf / f  # Maksymalnie dopuszczalny dryft
        react1 = 2 * dryft * (
                    1 + m)  # Maksymalna relatywna zmiana reaktancji na zaciskach C dla zmieszczenia sie w dryfcie
        RIA = ZIA.real * (
                    1 + (ZIA.imag / ZIA.real) ** 2)  # Rezystancja rownolegla obciazenia na poczatku procesu zgrzewania
        XIA = ZIA.imag  # Reaktancja rownolegla obciazenia na poczatku procesu zgrzewania
        RIIA = ZIIA.real * (
                    1 + (ZIIA.imag / ZIIA.real) ** 2)  # Rezystancja rownolegla obciazenia na koncu procesu zgrzewania
        XIIA = RIIA / (ZIIA.imag / ZIIA.real)  # Reaktancja rownolegla obciazenia na koncu procesu zgrzewania
        RIIC = 1 / (1 / RId - (1 - thetaIIo) / RId)  # Rezystancja reprezentujaca pobor mocy na koncu procesu zgrzewania
        squarepk = RIIA / RIIC  # Kwadrat przekladni transformatora WCz p i wspolczynnik sprzezenia
        x1 = 2 * dryft * (1 + m) / (
                    RIIA / RIIC * (1 / XIA - 1 / XIIA))  # Zakres zmian reaktancji na obwodzie pierwotnym
        # -------------------------------------------------------------------------------------------------------------

        # Dane wejsciowe do dokladnego obliczenia warunkow pracy generatora
        k = 0.316  # Wspolczynnik sprzezenia transformatora WCz
        #    p = 0.547 # Przekladnia transformatora WCz

        # -------------------------------------------------------------------------------------------------------------

        # Dokladne obliczenie warunkow pracy generatora dla 150 C
        rIIB = ZIIA.real / p ** 2
        xIIB = (ZIIA.imag / ZIIA.real) * rIIB
        ZIIC = complex(rIIB * k ** 2 * x1 ** 2 / (rIIB ** 2 + (x1 + xIIB) ** 2), x1 - (x1 + xIIB) * k ** 2 * x1 ** 2 / (
                    rIIB ** 2 + (
                        x1 + xIIB) ** 2))  # Impedancja wejsciowa transformatora obciazonego impedancja dla nagrzanego wsadu
        qIIC = ZIIC.imag / ZIIC.real  # Wspolczynnik reaktywnosci
        RIIC = qIIC ** 2 * ZIIC.real  # Rezystancja obciążenia przy T = 150 C wyliczona na podstawie parametrów transformatora i sprawnoci obwodu <Ohm>
        #    print('Rezystancja obciazenia na koniec procesu zgrzewania R** =', RIIC/1000, 'kOhm')
        PIIuz = 1000 * (Ua1 / 1000) ** 2 / (2 * (RIIC / 1000))  # Moc użyteczna na koncu procesu zgrzewania <W>
        P0str = ((1 - thetaIIo) / thetaIIo) * PIIuz  # Moc tracona w obwodzie
        R0 = Ua1 ** 2 / (2 * P0str)  # Rownolegla rezystancja strat <Ohm>
        Q0 = R0 / x1  # Minimalna dobroc obwodu nieobciazonego
        R0min = (RIIC * RId) / (RIIC - RId)  # Minimalna dopuszczalna przez triode rezystancja obciazenia
        Q0min = R0min / x1  # Minimalna dopuszczalna wartosc dobroci
        #    print('Minimalnie dopuszczalna wartosc dobroci Q0min =', Q0min)
        # -------------------------------------------------------------------------------------------------------------

        # Dokladne obliczenie warunkow generatora dla 20 C
        rIB = ZIA.real / p ** 2
        xIB = (ZIA.imag / ZIA.real) * rIB
        ZIC = complex(rIB * k ** 2 * x1 ** 2 / (rIB ** 2 + (x1 + xIB) ** 2), x1 - (x1 + xIB) * k ** 2 * x1 ** 2 / (
                    rIB ** 2 + (
                        x1 + xIB) ** 2))  # Impedancja wejsciowa transformatora obciazonego impedancja dla wsadu o temperaturze pokojowej
        qIC = ZIC.imag / ZIC.real  # Wspolczynnik reaktywnosci
        RIC = qIC ** 2 * ZIC.real  # Rezystancja obciążenia przy T = 20 C wyliczona na podstawie parametrów transformatora i sprawnoci obwodu <Ohm>
        #    print('Rezystancja obciazenia na poczatku procesu zgrzewania R* =', RIC/1000, 'kOhm')
        Puz = Ua1 ** 2 / (
                    2 * RIC)  # Moc dostarczona do linii przesylowej na poczatku procesu zgrzewania. Musi byc bliska do Puzmin
        #    print('Moc dostarczona do linii przesylowej na poczatku procesu zgrzewania Puz = ', Puz, 'W')
        # -------------------------------------------------------------------------------------------------------------

        # Wartosci poszczegolnych elementow generatora
        L1 = (159 / f) * x1 * 0.001  # Indukcyjnosc uzwojenia pierwotnego L1 <uH>
        #    print('Indukcyjnosc uzwojenia pierwotnego L1 =', L1, 'uH')
        L2 = p ** 2 * L1  # Indukcyjnosc uzwojenia wtornego L2 <uH>
        #    print('Indukcyjnosc uzwojenia wtornego L2 =', L2, 'uH')
        Ls = m * L1  # Indukcyjnosc sprzezenia zwrotnego
        xas = (1 + m) * x1  # Reaktancja kondensatora ukladu rezonansowego C <Ohm>
        C = (159 / f) / xas * 1000  # Pojemnosc kondesatora ukladu rezonansowego <pF>
        #    print('Pojemnosc kondensatora ukladu rezonansowego C =', C, 'pF')
        # -------------------------------------------------------------------------------------------------------------

        X.append(deltaf * 1000)
        Y.append(Q0min)

    return X, Y


p = 0.1
X, Y = CALC(p)
line = plt.plot(X, Y, color='black', label='p = 0.1')

p = 0.2
X, Y = CALC(p)
line = plt.plot(X, Y, color='blue', label='p = 0.2')

p = 0.3
X, Y = CALC(p)
line = plt.plot(X, Y, color='green', label='p = 0.3')

p = 0.4
X, Y = CALC(p)
line = plt.plot(X, Y, color='orange', label='p = 0.4')

p = 0.5
X, Y = CALC(p)
line = plt.plot(X, Y, color='gray', label='p = 0.5')

# plt.xlim(0, 500)
plt.ylim(0, 2200)
plt.xlabel('Dryft generatora, $\Delta f$ ($kHz$)')
# plt.xticks(np.arange(0, 500, step=50))
plt.ylabel('Dobroc rezonatora, $Q$')
plt.legend(loc='upper right')
plt.show()