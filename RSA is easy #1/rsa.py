import string

flag=''
e=65537
n=28150970547901913019901824364390497053600856369839321617996700606130553862041378369018779003752433356889118526332329074054728613209407037089320809898343953157935211086135010436283805891893636870991411236307901650696221491790470635225076251966300189483160148297407974155121570252648252906976186499329924342873
encryptedflag = [24603931406187071861602497345394097692989773194039735745762181586628499407802825983901643034231448504738113184470035863824128031443012073830520233613935485192804104698999763287388765215634314977991988580048221541560353418280294402691661980705832590960497587810514295642811714680627768268704899874164681718449, 11226318059664066669163529308725576208632153806776762372429671026861927737060205604020741904348343722215670471225630839065129589767356765848271000166982882271636977663052775953958080543340165408211633442938366994031562890034541604362383645601883118173819506187865617998294930587997187071040181458961091560176, 15645290594995180815865397749136800126080704684884296404807344870555186823350216705796063922278419585484662234210001661578549560411864952462380096494781766394542247609648743673312823946783517115542404474786395934886667795692210287283039316418126796934535150832709500306153601987121172178183970841498331059732, 24345863558959407738249127568820138362115734211146549194534219311913032290216606859385934708675962835857804566049600710875035366973110422262131331932310524891713319358676673958738776644229757625523955354996402750265022578843637525183704187498194489645838490640529841182709661371499013082259193633000753627261, 9620679224297488175028367924764722982789333194446063577221477359704180638294602848741035585656113543497776415635770748468725814916994577398023154224563920936523717884116880223345204061598438291740007518025998041449406726084042681798053863495542392481059281588020105313791046017356493739244555377217866496734, 1681724029430984846089508679185107538104072555994133932050319175633667369916570440070548756805254789524599169177371471218251246349461689959989338169394649813424706418737543924129213419625988100326558802566046751879531469160120914735332858786199496335523515150741728027296830843112416558460932541777024522279, 20629854768856798537062426042570334097651328955665698429979954410631113160492201197690192324881508105172595216229624523572595589920695165876501026993810936392510720968159305964832449680889041278532807173859579419197780294984519222830572413180237776797800176462492384318120546495539728732366110782215071262307, 7440918084186181327822271261394344901791253526257166181264874776746516620936925799031445704193589071453959493392065321806281801023425299535553522582376879027448581379760896052013060957519595664095702210758316558762834545655992756483227787274192094065257224706388623944855362716578806372564148647945479173348, 5097867843777034076271397095201528351784693372027998615436445410912131141882225577577253530396333413579756394884096318434100382509189974240357351425474190558456256750742731090012822064840481143528081027106843123030275420215136304130321013605031261372665636366377162666476737296028608455229357416005773064242, 10420107412794383499391199999666100864853724770814620968725971207705900061273163202891569477729023724554388008575891113425781557296798472693974759813058067631655217722786373465395279381307973425004404348124524059844749313287030234750535347511172780349725636807760402334957881556461382950021814486095167001394, 20895198446192697825002890636650624361863759520944494391240191454443921345578043873584884838772334163748883476104011030592329948454531053024873263786017045083052443924403769542324123323834338391361149767913830998218951574784777785739566046139742309557536025214334831372509789246522325522982945241815388133477, 11226318059664066669163529308725576208632153806776762372429671026861927737060205604020741904348343722215670471225630839065129589767356765848271000166982882271636977663052775953958080543340165408211633442938366994031562890034541604362383645601883118173819506187865617998294930587997187071040181458961091560176, 16657126895659048065404729920028465477385009450133540950695155983380795627778054526133891673615252510518969355629562948102050307259107355106086468465392660721567070464708776158039303608428552547481825035736610837329720474688421062759594907620576318249542577396722737724172954532394471909440668625218820801756, 11113777356910731413424023299582648618258376222028450254478672148119889617557563576704932635131420845868165014982665717620845578039880527701593963719893467068820107811384041511295664833904504511210342105242330522375476482706044695838957591685781703894244561607764476555630573446589408768780659378128082633769, 20895198446192697825002890636650624361863759520944494391240191454443921345578043873584884838772334163748883476104011030592329948454531053024873263786017045083052443924403769542324123323834338391361149767913830998218951574784777785739566046139742309557536025214334831372509789246522325522982945241815388133477, 1681724029430984846089508679185107538104072555994133932050319175633667369916570440070548756805254789524599169177371471218251246349461689959989338169394649813424706418737543924129213419625988100326558802566046751879531469160120914735332858786199496335523515150741728027296830843112416558460932541777024522279, 5237767970074646857079948735567615361735616179074197239639640947679550920349684166643572837235712904929824521258264241503059989875517915784117038966236672390569320206379357882906463342282254405974383459878863044723383164329146669331810709270455492110346838097216174137176255793792848357953314563364460847842, 20895198446192697825002890636650624361863759520944494391240191454443921345578043873584884838772334163748883476104011030592329948454531053024873263786017045083052443924403769542324123323834338391361149767913830998218951574784777785739566046139742309557536025214334831372509789246522325522982945241815388133477, 2141625583250052666579569568613448089970148215959031795439930595139028085767825695294403905882459409861220995951141855281841435481587946825079031782977651718402048988278639212978854590412709087674713750292922397103941195760574072700517109381299788645871729355745594573785064162048047595009933642068871994670, 278354276293884030290100330445865286604723740111170856624965259573282278044823323212960304154629174664076141280100412502135750130875356944835909175355370317285768658282746817782130476757714384697086179400629156643250500432197002583758692394681401772203578628635926749457621478296182304772136118691761841359, 6039667595601233082552071610487048398346324705021423176423484623705376133358539134558362499891954091431687578305623106726900655384011241742715735786166290331136153240702822544221903404870992713778423167867663948083662620087859096707381620051266745156545213726214080049764382107442159825610310695543673475542, 21353765873487781085375016306418205544750755310255410963646737671193146222650262290683259548572190880304009015662963424520575937651278866672082973874806201031606257157229306007587966460187818647603633973019548401357989358306250139692325474674826791149726161678649996852062656272851387461089863388359261125336, 11226318059664066669163529308725576208632153806776762372429671026861927737060205604020741904348343722215670471225630839065129589767356765848271000166982882271636977663052775953958080543340165408211633442938366994031562890034541604362383645601883118173819506187865617998294930587997187071040181458961091560176, 20576388598886140095325204584799302384454378372204683348252463729525849583734948105765087991438423260690623246579570440405616572326057536248148020737810766134083795050076636686776809469271643188562482921546497071402873405706504773345621716428511481598704631451463399778602486417840466985891815649711178813963, 17347447662661486040040289855519394974371562320877472776529836975445205017304164550202099250096382852783253959549113036367974281750823938616836362593312254792770954856762797438690474329666549947795964992533463700161635382925555835347885819042031312006167190561233042383984087765920275010577545908085026177611, 11788628214684738246695632901992250075758959059858474645166125685861157046466064692980236734739634298802473894878268029860203026238925142258303727438570051822763330338744774300757888262747314093511013562545738571326771345495509434761853742569509480619380000424215527153118231084573851377049921456961916278761, 20895198446192697825002890636650624361863759520944494391240191454443921345578043873584884838772334163748883476104011030592329948454531053024873263786017045083052443924403769542324123323834338391361149767913830998218951574784777785739566046139742309557536025214334831372509789246522325522982945241815388133477, 2141625583250052666579569568613448089970148215959031795439930595139028085767825695294403905882459409861220995951141855281841435481587946825079031782977651718402048988278639212978854590412709087674713750292922397103941195760574072700517109381299788645871729355745594573785064162048047595009933642068871994670, 2710029303357232932696197225263692040597986927359269224740812600224998707144266259851604978553286889767425982708691908438984279442981540971935737617354609856642312100797081348174935195638083002333058089328102430432526612805955273581245352312630845237670744276402867230550537275379675828467791243032108754996, 19981107233593350929447953514006501458466479260151660185153999799085657467921097940751860717309377498501638075002136637344148955811617399850718322497572421311807629329642551519284713638882025500074565475569618691516951449764680555447185364165687596161053684299589053909233984617244886185728811651967713024530, 3975884358027162862622932959187611984655247354547659825042810425039322096401899672988989768997134724085482147901304365437476311647149733392577446833370358728610677436154877051592307539990184750467273668379065865808900410057533079113476991204462719784464847498582643056503810805516315622314948257403761762299, 6039667595601233082552071610487048398346324705021423176423484623705376133358539134558362499891954091431687578305623106726900655384011241742715735786166290331136153240702822544221903404870992713778423167867663948083662620087859096707381620051266745156545213726214080049764382107442159825610310695543673475542, 14296542628093736444815382636071360035549021313467366701986569710120268508807886041986007828960248665683292143486565404978073122476968882030310174125355932205646388813061197657253533595700948593692407928813318978600474254105007396254987998953819782624738628334271910759242195864082910860797444993756044746481, 20895198446192697825002890636650624361863759520944494391240191454443921345578043873584884838772334163748883476104011030592329948454531053024873263786017045083052443924403769542324123323834338391361149767913830998218951574784777785739566046139742309557536025214334831372509789246522325522982945241815388133477, 7983594351048693624291138893287137601848867970873700373034058935656045095987011116108642350616654713531373295621458596238107660073931212524833777531450461876588350132328332972361857441613098452082271331281504722310376573085001395356078670960667878342134517577992585442881605030717788248137764480486762452442, 7983594351048693624291138893287137601848867970873700373034058935656045095987011116108642350616654713531373295621458596238107660073931212524833777531450461876588350132328332972361857441613098452082271331281504722310376573085001395356078670960667878342134517577992585442881605030717788248137764480486762452442, 23267174349531278768420819619439317179083929128083924515569762521057285892931325108327037262091624670335579302436476096123152288550738706103166820604983405317430467198343871458522070337902643863890959573514405066297449924638838605501211486861582957963752388608487593217237563529201436917108304692859773404548]
for encryptedchar in encryptedflag:
    for j in string.printable:
        if encryptedchar == pow(ord(j), e, n):
            flag = flag+j
print(flag)
