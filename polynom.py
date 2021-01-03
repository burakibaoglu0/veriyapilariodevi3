from time import time         
start_time = time()             #programımızın çalısma suresini görebilmek icin olusturdugumuz baslangıc zaman degeri
class _PolinomNode(object):
    """
     Polinom listesi için terim düğüm yapısı:
     us: polinomun tek bir terim derecesi
     katsayı: polinomun tek bir teriminin katsayısı.
     """
    def __init__(self, us, katSayi):
        self.us = us            #polinomun derecesi=üs değerini tutuyor
        self.katSayi = katSayi  #polinomun katsayısını tutuyor
        self.next = None


class Polinom:
    """
   Polinom, bir veya daha fazla terimden oluşturulmuş bir değişkenin matematiksel ifadesidir. 
   Her terim w_i * x ^ i biçimindedir, burada w_i skaler bir katsayıdır ve x ^ i, 
   i derecesinin değişkenidir. 
   """

    def __init__(self, us=None, katSayi=None):
        """     
 
        Varsayılan parametreler kullanılarak:
        1) Boş olarak başlatılan ve terim içermeyen yeni bir polinom oluşturur.
        2)Derece ve katsayı değişkenlerinden oluşturulan tek bir terimle
    başlatılan yeni bir polinom oluşturur.
        """

        if us is None:             
            self._poliHead = None           #O(n)->Erişim sağlandığı için
        else:      
            self._poliHead = _PolinomNode(us, katSayi)     #O(n)->Erişim sağlandığı için
        self._poliTail = self._poliHead                    #O(1)

    def us(self):
        """
        Polinomun derecesini verir (bir terim değil, yani tüm terimlerin en büyük derecesi). 
        Polinom terim içermiyorsa -1 değeri döndürülür.
        """
        if self._poliHead is None:       #O(n)->Erişim sağlandığı için
            return -1
        else:
            return self._poliHead.us     #O(n)->Erişim sağlandığı için

    def evaluate(self, scalar):
        """
        Polinomu verilen skaler değerde değerlendirir ve sonucu verir. 
        Boş bir polinom değerlendirilemez.
        """
        if self.us() >= 0:             #O(n)->Erişim sağlandığı için
            "Sadece boş olmayan polinomlar değerlendirilebilir."

        result = 0.0

        derNode = self._poliHead
        while derNode is not None:
            result += derNode.katSayi* (scalar ** derNode.us)        #O(n)
            derNode = derNode.next

        return result
       
    def __add__(self, eklPoli):
        """
        Bu polinomu ve eklPoli'yi eklemenin sonucu olan yeni bir Polinom oluşturur ve döndürür.
        Bu işlem, polinomlardan herhangi biri boşsa tanımlanmaz.
        """
        if self.us() >= 0 and eklPoli.us() >= 0 :        #O(n)->Erişim sağlandığı için
            "Toplamaya yalnızca boş olmayan polinomlarda izin verilir."

        yeniPolinom = Polinom()                  
        nodeA = self._poliHead          #O(n)+O(1)->Erişim sağlandığı ve atama yaptığı için
        nodeB = eklPoli._poliHead       #O(1)->Atama yaptığı için

        while nodeA is not None and nodeB is not None:  
            if nodeA.us > nodeB.us:              #O(1)
                us = nodeA.us                    
                katSayi = nodeA.katSayi
                nodeA = nodeA.next
            elif nodeA.us < nodeB.us:            #O(1)
                us = nodeB.us
                katSayi = nodeB.katSayi
                nodeB = nodeB.next
            else:                                #O(1)
                us = nodeA.us  # ya da  us = nodeB.us
                katSayi = nodeA.katSayi + nodeB.katSayi
                nodeA = nodeA.next
                nodeB = nodeB.next

            yeniPolinom._append(us, katSayi)          #O(1)->Ekleme işlemi yapıldığı için

        while nodeA is not None:
            yeniPolinom._append(nodeA.us, nodeA.katSayi)    #O(1)->Ekleme işlemi yapıldığı için
            nodeA = nodeA.next

        while nodeB is not None:
            yeniPolinom._append(nodeB.us, nodeB.katSayi)     #O(1)->Ekleme işlemi yapıldığı için
            nodeB = nodeB.next

        return yeniPolinom                  

    def __sub__(self, eklPoli):
        """__Add __ () yöntemiyle hemen hemen aynıdır; düğümA'nın derecesi 
        düğüm B'nin derecesinden daha küçük olduğunda, yeni katsayı-düğümB katsayısı olacaktır.
        """
        if self.us() >= 0 and eklPoli.us() >= 0:
            "Çıkarmaya yalnızca boş olmayan polinomlarda izin verilir."

        yeniPolinom = Polinom()
        nodeA = self._poliHead
        nodeB = eklPoli._poliHead

        while nodeA is not None and nodeB is not None:
            if nodeA.us > nodeB.us:       #O(1)
                us = nodeA.us
                katSayi = nodeA.katSayi
                nodeA = nodeA.next
            elif nodeA.us < nodeB.us:    #O(1)
                us = nodeB.us
                katSayi = -nodeB.katSayi  # B düğümündeki kat sayının çıkarma için - ile çarpılması
                nodeB = nodeB.next
            else:
                us = nodeA.us  # ya da us = nodeB.katSayi

                #A ve B'nin konumunu değiştiremez
                katSayi = nodeA.katSayi - nodeB.katSayi
                nodeA = nodeA.next
                nodeB = nodeB.next

            yeniPolinom._append(us, katSayi)

        while nodeA is not None:
            yeniPolinom._append(nodeA.us, nodeA.katSayi)       #O(1)->Ekleme işlemi yapıldığı için
            nodeA = nodeA.next

        while nodeB is not None:
            yeniPolinom._append(nodeB.us, nodeB.katSayi)       #O(1)->Ekleme işlemi yapıldığı için
            nodeB = nodeB.next

        return yeniPolinom


    def _append(self, us, katSayi):
        """
    Bir polinom terimin derecesini ve katsayısını kabul eden yardımcı yöntem, 
    terimi depolamak için yeni bir düğüm oluşturur ve düğümü listenin sonuna ekler.
        """
        if katSayi != 0.0:
            newTerm = _PolinomNode(us, katSayi)
            if self._poliHead is None:          #O(n)->Erişim sağlandığı için
                self._poliHead = newTerm        
            else:
                self._poliTail.next = newTerm    #O(n)->Erişim sağlandığı için

            self._poliTail = newTerm          

    def printPoli(self):
       
        derNode = self._poliHead         #O(n)+O(1)->Erişim sağlandığı ve atama yaptığı için
        while derNode is not None:
            if derNode.next is not None:
                # sözlüğe dayalı dize biçimi.
                print ("%(katSayi)sx^%(us)s + " % {"katSayi": derNode.katSayi, "us": derNode.us})
            else:
                print ("%(katSayi)sx^%(us)s" % {"katSayi": derNode.katSayi, "us": derNode.us})
            
            derNode = derNode.next


if __name__ == "__main__":
    birinciPol = Polinom(0,0)      #soldaki değer üs sağdaki değer katsayı 5x^2
    birinciPol += Polinom(1, 3)     #soldaki değer üs sağdaki değer katsayı 3x^1
    birinciPol += Polinom(0, -10)   #soldaki değer üs sağdaki değer katsayı -10x^0


    ikinciPol = Polinom(1133,5675)       #soldaki değer üs sağdaki değer katsayı 2x^3
    ikinciPol += Polinom(2, 4)      #soldaki değer üs sağdaki değer katsayı 4x^2
    ikinciPol += Polinom(0, 3)      #soldaki değer üs sağdaki değer katsayı 3x^0

    PoliTop = birinciPol + ikinciPol   #O(1)->Atama yaptığı için
    PoliCik = birinciPol - ikinciPol   #O(1)->Atama yaptığı için
    
    print ("İki polinomun toplamı:")
    PoliTop.printPoli()

    print ("İki polinomun çıkarılması:")
    PoliCik.printPoli()
    
end_time= time()                 #programın bitiş zamanının belirtimi
print(end_time - start_time)     #harcanan sürenin ekrana yazdırılımı



