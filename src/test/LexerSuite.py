import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_identifier1(self):
        self.assertTrue(TestLexer.test("aBc","aBc,<EOF>",101))
    
    def test_identifier2(self):
        self.assertTrue(TestLexer.test("1cjjd","1,cjjd,<EOF>",102))
    
    def test_identifier3(self):
        self.assertTrue(TestLexer.test("ajc_sjs","ajc_sjs,<EOF>",103))
    
    def test_identifier4(self):
        self.assertTrue(TestLexer.test("_!@#","_,Error Token !",104))
    
    def test_identifier5(self):
        self.assertTrue(TestLexer.test("___","___,<EOF>",105))

    def test_integer6(self):      
        self.assertTrue(TestLexer.test("1","1,<EOF>",106))
    
    def test_integer7(self):  
        self.assertTrue(TestLexer.test("01","01,<EOF>",107))
   
    def test_integer8(self):
        self.assertTrue(TestLexer.test("12cb289.90","12,cb289,.90,<EOF>",108))

    def test_real9(self):
        self.assertTrue(TestLexer.test(".1",".1,<EOF>",109))  
    
    def test_real10(self):
        self.assertTrue(TestLexer.test("1.2","1.2,<EOF>",110))
    
    def test_real11(self):
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",111))
    
    def test_real12(self):
        self.assertTrue(TestLexer.test("1e+2","1e+2,<EOF>",112))
    
    def test_real13(self):
        self.assertTrue(TestLexer.test("1.2e-2","1.2e-2,<EOF>",113))
    
    def test_real14(self):
        self.assertTrue(TestLexer.test("e12","e12,<EOF>",114))

    def test_comment15(self):
        self.assertTrue(TestLexer.test("//hjdshdjsd \r\n","<EOF>",115))
    
    def test_comment16(self):
        self.assertTrue(TestLexer.test("abc//comment \r\n","abc,<EOF>",116))
    
    def test_comment17(self):
        self.assertTrue(TestLexer.test("{comment}","<EOF>",117))

    def test_string18(self):
        self.assertTrue(TestLexer.test("\"\"",",<EOF>",118))  
    
    def test_string19(self):
        self.assertTrue(TestLexer.test("\"_!@#$%^\"","_!@#$%^,<EOF>",119))
    
    def test_string20(self):
        self.assertTrue(TestLexer.test("\"182mcelv03j.20\"","182mcelv03j.20,<EOF>",120))

    def test_keyword21(self):
        self.assertTrue(TestLexer.test("TRUE booolean","TRUE,booolean,<EOF>",121))
    
    def test_keyword22(self):
        self.assertTrue(TestLexer.test("tRuE bOolean","tRuE,bOolean,<EOF>",122))
    
    def test_keyword23(self):
        self.assertTrue(TestLexer.test("trU3 b0Ol3an","trU3,b0Ol3an,<EOF>",123))

    def test_operator24(self):
        self.assertTrue(TestLexer.test("+slc-slc*sj","+,slc,-,slc,*,sj,<EOF>",124))
    
    def test_operator25(self):
        self.assertTrue(TestLexer.test("+ - * $ % ^","+,-,*,Error Token $",125))
    
    def test_operator26(self):
        self.assertTrue(TestLexer.test("<= >= aNd oR == :=","<=,>=,aNd,oR,=,=,:=,<EOF>",126))
    
    def test_operator27(self):
        self.assertTrue(TestLexer.test("5+7*(9-3)/(6+7)","5,+,7,*,(,9,-,3,),/,(,6,+,7,),<EOF>",127))

    def test_seperator28(self):
        self.assertTrue(TestLexer.test("sdjksd,jksd:sdjska","sdjksd,,,jksd,:,sdjska,<EOF>",128))
    
    def test_seperator29(self):
        self.assertTrue(TestLexer.test(",.&,:",",,Error Token .",129))
    
    def test_seperator30(self):
        self.assertTrue(TestLexer.test("..(]{())","..,(,],Error Token {",130))

    def test_illegal_string31(self):
        self.assertTrue(TestLexer.test("\"sjcl{\j\s\m\d\s\tsjdk\"","Illegal Escape In String: sjcl{\\j",131))
   
    def test_error_token32(self):
        self.assertTrue(TestLexer.test("sh\j","sh,Error Token \\",132))
    
    def test_unclosed_string33(self):
        self.assertTrue(TestLexer.test("\"sjcjsl","Unclosed String: sjcjsl",133))   
    
    def test_unclosed_and_illegal34(self):
        self.assertTrue(TestLexer.test("\"ahihi\nihaa\"","Unclosed String: ahihi",134))
    
    def test_unclosed_string_in_a_program35(self):
        input="""
        procedure foo(a,b:integer);
        var x:real; s:string;
        begin
          s:="abc;
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,:,real,;,s,:,string,;,begin,s,:=,Unclosed String: abc;"
        self.assertTrue(TestLexer.test(input,expect,135))

    def test_simple_program36(self):
        input ="""
        procedure foo (a,b:integer;c:real);     //name of procedure
        var x,y:real;   //this is a comment
        begin   {another comment}
        //comment again
            x=6;
            y=9*x+10000/3;
        end //end of program
        """
        expect = "procedure,foo,(,a,,,b,:,integer,;,c,:,real,),;,var,x,,,y,:,real,;,begin,x,=,6,;,y,=,9,*,x,+,10000,/,3,;,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,136))

    def test_funcall37(self):
        input="""
        procedure TFrmFormCreate(Sender: string);
        var
            Reg: string;
        begin
            DisconnectedText := "Disconnected.";
            ConnectingText := "Connecting...";
            ConnectedStatusText := "Connected.";
            UserName := "";
            Server := "127.0.0.2";
            Reg := TRegistry_Create;
            Reg_RootKey := HKEY_LOCAL_MACHINE;
            begin
                SecurityLayer := Reg_ReadInteger("SecurityLayer");
                UserAuthentication := Reg_ReadInteger("UserAuthentication");
                Reg_WriteInteger("SecurityLayer", 0);
                Reg_WriteInteger("UserAuthentication", 0);
            end
        end
        """
        expect="procedure,TFrmFormCreate,(,Sender,:,string,),;,var,Reg,:,string,;,begin,DisconnectedText,:=,Disconnected.,;,ConnectingText,:=,Connecting...,;,ConnectedStatusText,:=,Connected.,;,UserName,:=,,;,Server,:=,127.0.0.2,;,Reg,:=,TRegistry_Create,;,Reg_RootKey,:=,HKEY_LOCAL_MACHINE,;,begin,SecurityLayer,:=,Reg_ReadInteger,(,SecurityLayer,),;,UserAuthentication,:=,Reg_ReadInteger,(,UserAuthentication,),;,Reg_WriteInteger,(,SecurityLayer,,,0,),;,Reg_WriteInteger,(,UserAuthentication,,,0,),;,end,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,137))
                         
    def test_identifier38(self):
        self.assertTrue(TestLexer.test("\"\"\"\"\"",",,Unclosed String: ",138))
                                 
    def test_identifier39(self):
        self.assertTrue(TestLexer.test("\"conbocuoi\bconbocuoi\"","Illegal Escape In String: conbocuoi\b",139))
                                 
    def test_identifier40(self):
        self.assertTrue(TestLexer.test("(* {abcd(abcd)//}abcd*)","<EOF>",140))
                                 
    def test_identifier41(self):
        self.assertTrue(TestLexer.test("hehe","hehe,<EOF>",141))
                
    def test_complex42(self):
        input="""
        n = int(input())
        a1 = list(map(int, input().strip().split(\' \')))
        a2 = list(map(int, input().strip().split(\' \')))
        c1 = [0 for i in range(2 * n)]
        for i in range(2 * n):
            if i % 4 == 1 or i % 4 == 2:
                c1[i] = c1[i - 1] + a2[i // 2] * i;
            else:
                c1[i] = c1[i - 1] + a1[i // 2] * i;
                c2 = [0 for i in range(n)]
                c3 = [0 for i in range(n)]
                o = 2 * n - 4
                c2[0] = (2 * n - 2) * a1[n - 1] + (2 * n - 1) * a2[n - 1];
                c3[0] = (2 * n - 2) * a2[n - 1] + (2 * n - 1) * a1[n - 1];
                sums = a1[n - 1] + a2[n - 1];
                for i in range(1, n):
                    c2[i] = c2[i - 1] - sums + o * a1[n - i - 1] + (2 * n - 1) * a2[n - i - 1];
                    c3[i] = c3[i - 1] - sums + o * a2[n - i - 1] + (2 * n - 1) * a1[n - i - 1];
                    o -= 2;
                    sums += a1[n - i - 1] + a2[n - i - 1];                                       
                    ans = 0;
                    for i in range(n):
                        ste = 0;
                        if i == 0:
                            ste = c2[n - 1];
                        elif i % 2 == 0:
                            ste = c2[n - i - 1] + c1[i * 2 - 1];
                        else:
                            ste = c3[n - i - 1] + c1[i * 2 - 1];
                            if ans < ste:
                                ans = ste;
                                print(ans)
        """
        expect="n,=,int,(,input,(,),),a1,=,list,(,map,(,int,,,input,(,),Error Token ."
        self.assertTrue(TestLexer.test(input,expect,142))
                        
    def test_complex43(self):
        input="""
        int main()
        {
                long long n;
                cin >> n;
                long long a1[n];
                for (long long i = 0; i < n; i++)
                        cin >> a1[i];
                long long a2[n];
                for (long long i = 0; i < n; i++)
                        cin >> a2[i];
                long long c1[2 * n];
                c1[0] = 0;
                for (long long i = 1; i < 2 * n; i++)
                {
                        if (i % 4 == 1 || i % 4 == 2)
                        {
                                c1[i] = c1[i - 1] + a2[i / 2] * i;
                        }
                        else
                        {
                                c1[i] = c1[i - 1] + a1[i / 2] * i;
                        }
                }

                long long c2[n], c3[n];
                long long o = 2 * n - 4;
                c2[0] = (2 * n - 2) * a1[n - 1] + (2 * n - 1) * a2[n - 1];
                c3[0] = (2 * n - 2) * a2[n - 1] + (2 * n - 1) * a1[n - 1];
                long long sum = a1[n - 1] + a2[n - 1];
                for (long long i = 1; i < n; i++)
                {
                        c2[i] = c2[i - 1] - sum + o * a1[n - i - 1] + (2 * n - 1) * a2[n - i - 1];
                        c3[i] = c3[i - 1] - sum + o * a2[n - i - 1] + (2 * n - 1) * a1[n - i - 1];
                        o -= 2;
                        sum += a1[n - i - 1] + a2[n - i - 1];
                }
                long long ans = 0;
                for (long long i = 0; i < n; i++)
                {
                        long long ste = 0;
                        if (i == 0)
                        {
                                ste = c2[n - 1];
                        }
                        else if (i % 2 == 0)
                        {
                                ste = c2[n - i - 1] + c1[i * 2 - 1];
                        }
                        else
                        {
                                ste = c3[n - i - 1] + c1[i * 2 - 1];
                        }
                        if (ans < ste)
                                ans = ste;
                }
                cout << ans << endl;
                return 0;
        }
        """
        expect="int,main,(,),else,Error Token }"
        self.assertTrue(TestLexer.test(input,expect,143))
                        
    def test_complex44(self):
        input="""
        int main()
        {
                int n, m, q;
                cin >> n >> m >> q;
                string s1, s2;
                cin >> s1;
                cin >> s2;
                int arr[n][n];
                arr[0][0] = 0;
                int occ[n];
                for (int i = 0; i < n - m + 1; i++)
                {
                        bool flag = true;
                        for (int j = 0; j < m; j++)
                        {
                                if (s1[i + j] != s2[j])
                                {
                                        flag = false;
                                        break;
                                }
                        }
                        if (flag)
                                occ[i] = 1;
                        else
                                occ[i] = 0;
                }
                int l, r;
                for (int i = 0; i < q; i++)
                {
                        cin >> l >> r;
                        int ans = 0;
                        for (int j = l - 1; j < r - m + 1; j++)
                        {
                                ans += occ[j];
                        }
                        cout << ans << endl;
                }
                return 0;
        }
        """     
        expect="int,main,(,),Error Token }"
        self.assertTrue(TestLexer.test(input,expect,144))
                        
    def test_complex45(self):
        input="""
        bool cmp(pair<int, int> a, pair<int, int> b)
        {
                if (a.first < b.first)
                        return true;
                if (a.first == b.first && a.second < b.second)
                        return true;
                return false;
        }
        int main()
        {
                int n;
                cin >> n;
                vector<pair<int, int>> arr;
                pair<int, int> s;
                for (int i = 0; i < n; i++)
                {
                        cin >> s.first >> s.second;
                        arr.push_back(s);
                }
                sort(arr.begin(), arr.end(), cmp);
                int ar[2 * n];
                queue<int> q1, q2;
                int m = 0;
                bool flag = true;
                for (int i = 0; i < 2 * n && flag; i++)
                {
                        if (i < n)
                        {
                                q1.push(arr[i].first);
                                q2.push(arr[i].second);
                        }
                        if (q1.empty() && q2.empty())
                        {
                                flag = false;
                                break;
                        }
                        if (!q1.empty() && q1.front() < q2.front())
                        {
                                if (m != 0 && ar[m - 1] != q1.front())
                                {
                                        ar[m] = q1.front();
                                        m++;
                                }
                                if (m == 0)
                                {
                                        ar[m] = q1.front();
                                        m++;
                                }
                                q1.pop();
                        }
                        else
                        {
                                if (ar[m - 1] != q2.front())
                                {
                                        ar[m] = q2.front();
                                        m++;
                                }
                                q2.pop();
                        }
                }
                for (int i = 0; i < m; i++)
                        cout << ar[i] << " ";
                cout << endl;
                int b = 0;
                int t = 0;
                int br[m], cr[m];
                for (int i = 0; i < m; i++)
                {
                        br[i] = 0;
                        cr[i] = 0;
                }
                for (int i = 0; i < n; i++)
                {
                        while (arr[i].first > ar[b])
                                b++;
                        int c = b;
                        while (c < m - 1 && arr[i].second > ar[c])
                        {
                                br[c]++;
                                c += 1;
                        }
                        t = i;
                }
                for (int i = 0; i < m - 1; i++)
                        cout << br[i] << " ";
                cout << endl;
                for (int i = 0; i < m; i++)
                        cout << cr[i] << " ";
                cout << endl;
                long long ans[n];
                for (int i = 0; i < n; i++)
                        ans[i] = 0;
                for (int i = 0; i < m - 1; i++)
                {
                        ans[br[i] - 1] += ar[i + 1] - ar[i] - 1;
                }
                for (int i = 0; i < m; i++)
                {
                        ans[cr[i] - 1]++;
                }
                for (int i = 0; i < n; i++)
                        cout << ans[i] << " ";
                cout << endl;
                return 0;      
        """
        expect="bool,cmp,(,pair,<,int,,,int,>,a,,,pair,<,int,,,int,>,b,),int,main,(,),sort,(,arr,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,145))
                        
    def test_complex46(self):
        input="""
        int main()
        {
                int n;
                cin >> n;
                pair<long long, int> s;
                vector<pair<long long, int>> arr;
                for (int i = 0; i < n; i++)
                {
                        cin >> s.first;
                        s.second = 1;
                        arr.push_back(s);
                        cin >> s.first;
                        s.first++;
                        s.second = -1;
                        arr.push_back(s);
                }
                sort(arr.begin(), arr.end());
                long long ans[n + 1];
                for (int i = 0; i < n + 1; i++)
                        ans[i] = 0;
                int t = 0;
                for (int i = 0; i < 2 * n - 1; i++)
                {
                        t += arr[i].second;
                        ans[t] += arr[i + 1].first - arr[i].first;
                }
                for (int i = 1; i < n + 1; i++)
                {
                        cout << ans[i] << " ";
                }
                cout << endl;
                return 0;
        }
        }
        """
        expect="int,main,(,),sort,(,arr,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,146))
                        
    def test_complex47(self):
        input="""
        int main()
        {
                int n, m;
                cin >> n >> m;
                int arr[n + 1];
                for (int i = 0; i < n; i++)
                {
                        cin >> arr[i];
                }
                arr[n] = m;
                int f1[n + 1], f2[n + 1];
                f1[0] = arr[0];
                f2[0] = 0;
                for (int i = 1; i < n + 1; i++)
                {
                        if (i % 2 == 1)
                        {
                                f1[i] = f1[i - 1];
                                f2[i] = f2[i - 1] + arr[i] - arr[i - 1];
                        }
                        else
                        {
                                f1[i] = f1[i - 1] + arr[i] - arr[i - 1];
                                f2[i] = f2[i - 1];
                        }
                }
                int ans = f1[n];
                for (int i = 0; i < n + 1; i++)
                {
                        m = 0;
                        if (i % 2 == 0)
                        {
                                m = ((i == 0) ? 0 : f1[i - 1]) + arr[i] - ((i == 0) ? 0 : arr[i - 1]) - 1 + f2[n] - f2[i];
                        }
                        else
                        {
                                m = f1[i] + arr[i] - arr[i - 1] - 1 + f2[n] - f2[i];
                        }
                        if (ans < m)
                        {
                                ans = m;
                                cout << "a " << i << endl;
                        }
                }
                cout << f1[3] + arr[3] - 1 + f2[n] - f2[3] << endl;
                cout << ans << endl;
                for (int i = 0; i < n + 1; i++)
                        cout << f1[i] << " ";
                cout << endl;
                for (int i = 0; i < n + 1; i++)
                        cout << f2[i] << " ";
                cout << endl;
                return 0;
        }
        """
        expect="int,main,(,),arr,[,n,],=,m,;,int,f1,[,n,+,1,],,,f2,[,n,+,1,],;,f1,[,0,],=,arr,[,0,],;,f2,[,0,],=,0,;,for,(,int,i,=,1,;,i,<,n,+,1,;,i,+,+,),else,Error Token }"
        self.assertTrue(TestLexer.test(input,expect,147))
                        
    def test_complex48(self):
        input="""
        int min(int a, int b)
        {
                if (a > b)
                        return b;
                return a;
        }
        int style(string s)
        {
                if (s == "M")
                        return 1;
                if (s == "S")
                        return 2;
                if (s == "L")
                        return 3;
                if (s == "XS")
                        return 4;
                if (s == "XL")
                        return 5;
                if (s == "XXS")
                        return 6;
                if (s == "XXL")
                        return 7;
                if (s == "XXXS")
                        return 8;
                if (s == "XXXL")
                        return 9;
                return 0;
        }
        int main()
        {
                int n;
                cin >> n;
                string s;
                int ar[10];
                for (int i = 0; i < 10; i++)
                        ar[i] = 0;
                for (int i = 0; i < n; i++)
                {
                        cin >> s;
                        ar[style(s)]++;
                }
                int br[10];
                for (int i = 0; i < 10; i++)
                        br[i] = 0;
                for (int i = 0; i < n; i++)
                {
                        cin >> s;
                        br[style(s)]++;
                }
                int ans = 0;
                int t = 0;
                int sum = 0;
                for (int i = 1; i < 10; i++)
                {
                        t += min(ar[i], br[i]);
                        sum += ar[i];
                }
                ans = sum - t;
                cout << ans << endl;
                return 0;
        }
        """
        expect="int,min,(,int,a,,,int,b,),int,style,(,string,s,),int,main,(,),int,br,[,10,],;,for,(,int,i,=,0,;,i,<,10,;,i,+,+,),br,[,i,],=,0,;,for,(,int,i,=,0,;,i,<,n,;,i,+,+,),int,ans,=,0,;,int,t,=,0,;,int,sum,=,0,;,for,(,int,i,=,1,;,i,<,10,;,i,+,+,),ans,=,sum,-,t,;,cout,<,<,ans,<,<,endl,;,return,0,;,Error Token }"
        self.assertTrue(TestLexer.test(input,expect,148))
                        
    def test_complex49(self):
        input="""
        int main()
        {
                int n, m;
                cin >> n >> m;
                int r[n];
                int xor_r = 0;
                for (int i = 0; i < n; i++)
                {
                        cin >> r[i];
                        xor_r ^= r[i];
                }
                int c[m];
                int xor_c = 0;
                for (int i = 0; i < m; i++)
                {
                        cin >> c[i];
                        xor_c ^= c[i];
                }
                if (xor_c != xor_r)
                {
                        cout << "NO" << endl;
                        return 0;
                }
                cout << "YES" << endl;
                int final_o = 0;
                for (int i = 0; i < n - 1; i++)
                {
                        int s = 0;
                        for (int j = 0; j < m - 1; j++)
                        {
                                cout << 1 << " ";
                                s ^= 1;
                        }
                        final_o ^= r[i] ^ s;
                        cout << (r[i] ^ s) << endl;
                }
                for (int j = 0; j < m - 1; j++)
                {
                        cout << (((n - 1) % 2) ^ c[j]) << " ";
                }
                cout << (c[m - 1] ^ final_o) << endl;
                return 0;
        }
        """
        expect="int,main,(,),int,c,[,m,],;,int,xor_c,=,0,;,for,(,int,i,=,0,;,i,<,m,;,i,+,+,),if,(,xor_c,Error Token !"
        self.assertTrue(TestLexer.test(input,expect,149))
                        
    def test_complex50(self):
        input="""
        int main()
        {
                int n, m;
                cin >> n >> m;
                int arr[n];
                for (int i = 0; i < n; i++)
                        cin >> arr[i];
                int s = 0;
                for (int i = 0; i < n; i++)
                {
                        s += arr[i];
                        cout << s / m << " ";
                        s %= m;
                }
                cout << endl;
                return 0;
        }
        """
        expect="int,main,(,),cout,<,<,endl,;,return,0,;,Error Token }"
        self.assertTrue(TestLexer.test(input,expect,150))
                                
    def test_complex51(self):
        input="""
        int t, n;
        string st;
        int main()
        {
                cin >> t;
                for (int i = 0; i < t; i++)
                {
                        cin >> n;
                        cin >> st;
                        bool kt = true;
                        for (int i = 0; i < n / 2; i++)
                        {
                                int j = n - i - 1;
                                if (!(st[i] == st[j] || st[i] - st[j] == 2 || st[j] - st[i] == 2))
                                {
                                        cout << "NO" << endl;
                                        kt = false;
                                        break;
                                }
                        }
                        if (kt)
                                cout << "YES" << endl;
                }
                return 0;
        }
        """
        expect="int,t,,,n,;,string,st,;,int,main,(,),Error Token }"
        self.assertTrue(TestLexer.test(input,expect,151))
                                
    def test_complex52(self):
        input="""
        long long x, y, q, n;
        int main()
        {
                cin >> n >> q;
                for (int i = 0; i < q; i++)
                {
                        cin >> y >> x;
                        long long t = 0;
                        t += ((y - 1) / 2) * n;
                        if (x % 2 == y % 2)
                        {
                                if (x % 2 == 0)
                                        t += (n + 1) / 2 + x / 2;
                                else
                                        t += (x + 1) / 2;
                        }
                        else
                        {
                                t += (n * n + 1) / 2;
                                if (x % 2 != 0)
                                        t += n / 2 + (x + 1) / 2;
                                else
                                        t += x / 2;
                        }
                        cout << t << endl;
                }
                return 0;
        }
        """
        expect="long,long,x,,,y,,,q,,,n,;,int,main,(,),else,cout,<,<,t,<,<,endl,;,Error Token }"
        self.assertTrue(TestLexer.test(input,expect,152))
                                
    def test_complex53(self):
        input="""
        int t, n, a[1000010], b[1000010], top;
        int main()
        {
                scanf("%d", &t);
                for (int k = 0; k < t; k++)
                {
                        scanf("%d", &n);
                        for (int j = 0; j < n; j++)
                        {
                                scanf("%d", a + j);
                        }
                        sort(a, a + n);
                        top = 0;
                        for (int i = 1; i < n; i++)
                                if (a[i] == a[i - 1])
                                {
                                        b[top++] = a[i];
                                        a[i] = a[i - 1] = -1;
                                }
                        int s = 1;
                        for (int i = 2; i < top; i++)
                        {
                                if (1ll * b[i - 1] * b[s] > 1ll * b[s - 1] * b[i])
                                        s = i;
                        }
                        cout << b[s] << " " << b[s] << " " << b[s - 1] << " " << b[s - 1] << endl;
                        printf("%d %d %d %d", b[s], b[s], b[s - 1], b[s - 1]);
                }
                return 0;
        }
        """
        expect="int,t,,,n,,,a,[,1000010,],,,b,[,1000010,],,,top,;,int,main,(,),sort,(,a,,,a,+,n,),;,top,=,0,;,for,(,int,i,=,1,;,i,<,n,;,i,+,+,),if,(,a,[,i,],=,=,a,[,i,-,1,],),int,s,=,1,;,for,(,int,i,=,2,;,i,<,top,;,i,+,+,),cout,<,<,b,[,s,],<,<, ,<,<,b,[,s,],<,<, ,<,<,b,[,s,-,1,],<,<, ,<,<,b,[,s,-,1,],<,<,endl,;,printf,(,%d %d %d %d,,,b,[,s,],,,b,[,s,],,,b,[,s,-,1,],,,b,[,s,-,1,],),;,Error Token }"
        self.assertTrue(TestLexer.test(input,expect,153))
                                
    def test_complex54(self):
        input="""
        int n, c[200020], a[200010], d[200010], ans = 0;
        int main()
        {
                cin >> n;
                for (int i = 0; i < n; i++)
                        cin >> c[i];
                for (int i = 0; i < n; i++)
                {
                        cin >> a[i];
                        a[i]--;
                        d[i] = 0;
                }
                for (int i = 0; i < n; i++)
                {
                        if (d[i])
                                continue;
                        int cur = i;
                        vector<int> s;
                        while (!d[cur])
                        {
                                s.push_back(cur);
                                d[cur] = 1;
                                cur = a[cur];
                        }
                        bool loop = false;
                        for (int j = 0; j < s.size(); j++)
                        {
                                if (s[j] == cur)
                                {
                                        loop = true;
                                        break;
                                }
                        }
                        if (loop)
                        {
                                int t = cur, k = c[cur];
                                cur = a[cur];
                                while (cur != t)
                                {
                                        if (k > c[cur])
                                                k = c[cur];
                                        cur = a[cur];
                                }
                                ans += k;
                        }
                }
                cout << ans << endl;
                return 0;
        }
        """
        expect="int,n,,,c,[,200020,],,,a,[,200010,],,,d,[,200010,],,,ans,=,0,;,int,main,(,),for,(,int,i,=,0,;,i,<,n,;,i,+,+,),bool,loop,=,false,;,for,(,int,j,=,0,;,j,<,s,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,154))
                
    def test_complex55(self):
        input="""
        int n, k, P = 998244353;
        int main() {}
        """
        expect="int,n,,,k,,,P,=,998244353,;,int,main,(,),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,155))
                        
    def test_complex56(self):
        input="""
        n = int(input())
        s = map(int, input().strip().split(' '))
        t = [0 for i in range(101)]
        for i in s:    t[i] += 1
        print(max(t))  
        """
        expect="n,=,int,(,input,(,),),s,=,map,(,int,,,input,(,),Error Token ."
        self.assertTrue(TestLexer.test(input,expect,156))
                        
    def test_complex57(self):
        input="""
        def f(a, b, x):
            if x == 1:
                return a * "0" + b * "1" 
                if x == 2:
                return "0" + b * "1" + (a - 1) * "0"
                if x % 2 == 1:
                        return "01" * int(x/2) + "0" * (a - int(x/2)) + "1" * (b - int(x/2))
                        return "01" * int(x/2) + "1" * (b - int(x/2)) + "0" * (a - int(x/2))
                        [a, b, x] = map(int, input().strip().split())if a < b:
                                ansa = f(b, a, x)
                                ansb = ''.join([str(1 - int(i)) for i in ansa])
                                print(ansb)else:
                                    print(f(a,b,x))   
        """
        expect="def,f,(,a,,,b,,,x,),:,if,x,=,=,1,:,return,a,*,0,+,b,*,1,if,x,=,=,2,:,return,0,+,b,*,1,+,(,a,-,1,),*,0,if,x,Error Token %"
        self.assertTrue(TestLexer.test(input,expect,157))
                        
    def test_complex58(self):
        input="""
        def f(seg, k):
                c = sum(seg[:k])
                m = c
                for i in range(k, len(seg)):
                        c = c - seg[i - k] + seg[i]
                        m = max(m, c)
                        return m/k
                        def g(seg, k):
                                t = [f(seg, i) for i in range(k, len(seg) + 1)]
                                return max(t)
                                [n, k] = list(map(int, input().strip().split(' ')))
                                seg = list(map(int, input().strip().split(' ')))
                                print(g(seg, k))      
        """
        expect="def,f,(,seg,,,k,),:,c,=,sum,(,seg,[,:,k,],),m,=,c,for,i,in,range,(,k,,,len,(,seg,),),:,c,=,c,-,seg,[,i,-,k,],+,seg,[,i,],m,=,max,(,m,,,c,),return,m,/,k,def,g,(,seg,,,k,),:,t,=,[,f,(,seg,,,i,),for,i,in,range,(,k,,,len,(,seg,),+,1,),],return,max,(,t,),[,n,,,k,],=,list,(,map,(,int,,,input,(,),Error Token ."
        self.assertTrue(TestLexer.test(input,expect,158))
                        
    def test_complex59(self):
        input="""
        def f(i):
            k = 0
            while i != 1:
                k += 1
                i = int(i/2)
                return k
            [n, q] = map(int, input().strip().split())
            coin = list(map(int, input().strip().split()))
            coin_bin = sorted([f(i) for i in coin])
            ns = [0 for i in range(33)]for i in coin_bin:
                ns[i] += 1
                for j in range(q):
                    qs = int(input)
                    qs_bin = bin(qs)[2:]
                    lqs = len(qs_bin)
                    ks = ns
                    ans = 0
                    for i in range(lqs):
                        index = lqs - i - 1
                        if qs_bin[index] == "1":
                                if ks[i] == 0:
                                        print(-1)
                                        break
                                        ans += 1
                                        ks[i + 1] != (ks[i] - 1) / 2    
        """
        expect="def,f,(,i,),:,k,=,0,while,i,Error Token !"
        self.assertTrue(TestLexer.test(input,expect,159))
                        
    def test_complex60(self):
        input="""
        def f(i):
                k = 0
                while i != 1:
                        k += 1
                        i = int(i/2)
                        return kdef
                finds(l, i, n):
                        if i == 0:
                                if l[0] >= n:
                                        l[0] -= n
                                        return (l, n)
                                return (l, -1)
                        if l[i] < n:
                                p = finds(l, i - 1, (n - l[i]) * 2)
                                if p[1] == -1:
                                        return (l, -1)
                                l = p[0]
                                k = l[i]
                                l[i] = 0
                                return (l, p[1] + k)
                        l[i] -= n
                        return (l, n)
                [n, q] = map(int, input().strip().split())
                coin = list(map(int, input().strip().split()))
                coin_bin = [f(i) for i in coin]
                ns = [0 for i in range(33)]for i in coin_bin:
                        ns[i] += 1
                        for j in range(q):
                                qs = int(input())
                                qs_bin = bin(qs)[2:]
                                lqs = len(qs_bin)
                                ks = [i for i in ns]
                                ans = 0 
                                for i in range(lqs):
                                        if qs_bin[i] == '1':
                                                np = lqs - i - 1
                                                p = finds(ks, np, 1)
                                                if p[1] == -1: 
                                                        ans = -1  
                                                        break                                                           
        """
        expect="def,f,(,i,),:,k,=,0,while,i,Error Token !"
        self.assertTrue(TestLexer.test(input,expect,160))
                        
    def test_complex61(self):
        input = """
        Var a,b:integer;
        sdsd:real;
        function test():integer;
        var x,y:real;
        begin
        end
        """
        expect="Var,a,,,b,:,integer,;,sdsd,:,real,;,function,test,(,),:,integer,;,var,x,,,y,:,real,;,begin,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,161))
                
    def test_complex62(self):
        input="""
        procedure foo (a,b: integer;c: real);
        var x,y: real;
        begin
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,;,c,:,real,),;,var,x,,,y,:,real,;,begin,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,162))
                        
    def test_complex63(self):
        input="""
        procedure foo (a,b: integer);
        var x,y: real;
        begin
        end
        procedure main();
        //this is a comment
        var a,b: integer;
        begin
        foo();
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,,,y,:,real,;,begin,end,procedure,main,(,),;,var,a,,,b,:,integer,;,begin,foo,(,),;,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,163))
                        
    def test_complex64(self):
        input="""
        procedure foo (a,b: integer);
        var x,y: real;
        begin
        end
        procedure main();
        //this is a comment
        var a,b: integer;
        begin
            a:= 1;
            for i:=1 to 5 do
            begin
                pritnt(a);
                 foo(a,b);
            end                   
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,,,y,:,real,;,begin,end,procedure,main,(,),;,var,a,,,b,:,integer,;,begin,a,:=,1,;,for,i,:=,1,to,5,do,begin,pritnt,(,a,),;,foo,(,a,,,b,),;,end,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,164))
                        
    def test_complex65(self):
        input="""
        procedure foo (a,b: integer);
        var x,y: real;
        begin
        end

        procedure main();
        //this is a comment
        var a,b: integer;
            c:array [1 .. 2] of real;
        begin
            a:= 1;
            if a>1 then
                foo(a,b);
            else 
                a := foo(a,b)+3;
            while a=1 do a:=c-b;
            for i:=1 to a*2 do foo(a,b);
            break;
            continue;
            return foo(a,b);
            with a:integer; b:real; do
            begin
                a:=foo(a,b);
                print(a);
            end

        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,,,y,:,real,;,begin,end,procedure,main,(,),;,var,a,,,b,:,integer,;,c,:,array,[,1,..,2,],of,real,;,begin,a,:=,1,;,if,a,>,1,then,foo,(,a,,,b,),;,else,a,:=,foo,(,a,,,b,),+,3,;,while,a,=,1,do,a,:=,c,-,b,;,for,i,:=,1,to,a,*,2,do,foo,(,a,,,b,),;,break,;,continue,;,return,foo,(,a,,,b,),;,with,a,:,integer,;,b,:,real,;,do,begin,a,:=,foo,(,a,,,b,),;,print,(,a,),;,end,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,165))
                        
    def test_complex66(self):
        input="""
        procedure foo(a,b:integer);
        var x:real;
        begin
            for a:=1 to n do
            begin
                if x >= 4 or  x < 4 then
                begin
                    foo(3);
                    a:=1;
                end
                else 
                begin
                    foo(1.);
                    1l.2e-!2;
                end
            end
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,:,real,;,begin,for,a,:=,1,to,n,do,begin,if,x,>=,4,or,x,<,4,then,begin,foo,(,3,),;,a,:=,1,;,end,else,begin,foo,(,1.,),;,1,l,.2,e,-,Error Token !"
        self.assertTrue(TestLexer.test(input,expect,166))
                        
    def test_complex67(self):
        input="""
        procedure foo(a,b:integer);
        var x:real;
        begin
            for a:=1 to n do
            begin
                if x >= 4 or  x < 4 then
                begin
                    foo(3);
                    a:=1;
                end
                else 
                begin
                    foo(1.);
                    ;
                end
            end
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,:,real,;,begin,for,a,:=,1,to,n,do,begin,if,x,>=,4,or,x,<,4,then,begin,foo,(,3,),;,a,:=,1,;,end,else,begin,foo,(,1.,),;,;,end,end,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,167))
          
    def test_complex68(self):
        input="""
        procedure foo(a,b:integer);
        var x:real;
        begin
            foo(-+3);
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,:,real,;,begin,foo,(,-,+,3,),;,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,168))
                    
    def test_complex69(self):
        input="""
        procedure foo(a,b:integer);
        var x:real;
        begin
            for a:=1,b:=2 to n do foo(a,b);  
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,:,real,;,begin,for,a,:=,1,,,b,:=,2,to,n,do,foo,(,a,,,b,),;,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,169))
                    
    def test_complex70(self):
        input="""
         procedure foo(a,b:integer);
        var x:real;
        begin
            a:=1;
            x:= + 1;
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,:,real,;,begin,a,:=,1,;,x,:=,+,1,;,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,170))
                    
    def test_complex71(self):
        input="""
        procedure foo(a,b:integer);
        var x:real;
        begin
            a[.2e+12 + 3] := 3;
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,:,real,;,begin,a,[,.2e+12,+,3,],:=,3,;,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,171))
                    
    def test_complex72(self):
        input="""
        procedure foo(a,b:integer);
        var x:real;
        begin
            a[.2e3 >= 5 < 12 + 3] := 3;
        end
        """
        expect="procedure,foo,(,a,,,b,:,integer,),;,var,x,:,real,;,begin,a,[,.2e3,>=,5,<,12,+,3,],:=,3,;,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,172))
                    
    def test_boolean_expression73(self):
        self.assertTrue(TestLexer.test("a+b>4","a,+,b,>,4,<EOF>",173))
    
    def test_boolean_expression74(self):
        self.assertTrue(TestLexer.test("false < true ","false,<,true,<EOF>",174))
    
    def test_boolean_expression75(self):
        self.assertTrue(TestLexer.test("__a__ __add__ __b__ __eq__ __c__","__a__,__add__,__b__,__eq__,__c__,<EOF>",175))
                      
    def test_token_quote_in_program76(self):
        self.assertTrue(TestLexer.test("a'sVN","a,Error Token '",176))
    
    def test_backslash_and_a_character_in_program77(self):
        self.assertTrue(TestLexer.test("\a","Error Token \a",177))
    
    def test_comment_without_closing_in_program78(self):
        self.assertTrue(TestLexer.test("ab//c{ad\ns}","ab,s,Error Token }",178))
    
    def test_exclamation_mark_in_program79(self):
        self.assertTrue(TestLexer.test("!@#","Error Token !",179))

    def test_using_line_feed_in_string80(self):
        self.assertTrue(TestLexer.test("\"abc\\nxyz\"","abc\\nxyz,<EOF>",180))
    
    def test_using_carriage_return_in_string81(self):
        self.assertTrue(TestLexer.test("\"abc\\rxyz\"","abc\\rxyz,<EOF>",181))
    
    def test_using_tab_in_string82(self):
        self.assertTrue(TestLexer.test("\"abc\\txyz\"","abc\\txyz,<EOF>",182))
    
    def test_using_form_feed_in_string83(self):
        self.assertTrue(TestLexer.test("\"abc\\fxyz\"","abc\\fxyz,<EOF>",183))
    
    def test_using_backspace_in_string84(self):
        self.assertTrue(TestLexer.test("\"abc\\bxyz\"","abc\\bxyz,<EOF>",184))

    def test_assign_5_into_dash85(self):
        self.assertTrue(TestLexer.test("_=5","_,=,5,<EOF>",185))
    
    def test_C_var_declare86(self):
        self.assertTrue(TestLexer.test("int a=5","int,a,=,5,<EOF>",186))
    
    def test_MP_var_declare87(self):
        self.assertTrue(TestLexer.test("var i:integer;","var,i,:,integer,;,<EOF>",187))
    
    def test_import_CRT_library88(self):
        self.assertTrue(TestLexer.test("uses crt;","uses,crt,;,<EOF>",188))
   
    def test_simple_Pascal_program89(self):
        self.assertTrue(TestLexer.test("uses crt;\nvar i:integer;\n\tst:string;\nbegin\n\tclrscr;\n\tst=\"abcx\\tyz\";\n\twriteln(st);\nend","uses,crt,;,var,i,:,integer,;,st,:,string,;,begin,clrscr,;,st,=,abcx\\tyz,;,writeln,(,st,),;,end,<EOF>",189))
    
    def test_unicode_character90(self):
        self.assertTrue(TestLexer.test(str("var ◙=5;".encode("utf-8")),"b,Error Token '",190))
        
    def test_identifier91(self):
        self.assertTrue(TestLexer.test("anh met qua", "anh,met,qua,<EOF>", 191))
    
    def test_identifier92(self):
        self.assertTrue(TestLexer.test("anh muon di ngu", "anh,muon,di,ngu,<EOF>", 192))
    
    def test_identifier93(self):
        self.assertTrue(TestLexer.test("hon 12 gio roi", "hon,12,gio,roi,<EOF>", 193))
    
    def test_identifier94(self):
        self.assertTrue(TestLexer.test("ngay mai la thu 6", "ngay,mai,la,thu,6,<EOF>", 194))
    
    def test_identifier95(self):
        self.assertTrue(TestLexer.test("bai tap nhieu sml", "bai,tap,nhieu,sml,<EOF>", 195))
    
    def test_identifier96(self):
        self.assertTrue(TestLexer.test("oh yeah test cuoi cung roi di ngu thoi", "oh,yeah,test,cuoi,cung,roi,di,ngu,thoi,<EOF>", 196))

    def test_dot_in_program97(self):
        self.assertTrue(TestLexer.test(".","Error Token .",197))
    
    def test_at_sign_in_program98(self):
        self.assertTrue(TestLexer.test("@","Error Token @",198))
    
    def test_real_literal_without_digit_before_exponent_part99(self):
        self.assertTrue(TestLexer.test(".e2","Error Token .",199))
    
    def test_percent_sign_in_program100(self):
        self.assertTrue(TestLexer.test("^","Error Token ^",200))
    