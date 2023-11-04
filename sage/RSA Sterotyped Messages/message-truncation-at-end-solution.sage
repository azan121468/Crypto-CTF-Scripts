e = 3
N=16366151674641298826113801572264216562809964949522481732641785452585589156176183002220549207100835947022665995220360024205457959908369269338781625380563546834971975894349386087040568959667228096907681016269120136062941231275992087643636661672110586572398686073039143782051231470435637024007282231321527560134828928791826898070176809017064301234297582158484092429893511600369351103659817108891216990812332974719623383738485890721980555641824511547396250550238437164929542212015598726252958954135445058239225614884400485328323360475392002477122238603929611063473307683143722984370704642558115096024340754861231591966233
enc = 13118468061464045271313425043769793354730922474876630375841838658718850732577463779290017434570947581431212182022779320547002504941979130619030281333952278664641141231468183808264680217552088324764743536989568463476551305682617917549964642289903397025989515250075944814758309703037234187792756659905518106219436614994050103284488121221473932708213738415322614959573175143982727887083528140226910543441538685030103599595413591743605722951923550073581457721414034532641308873723542946496160751044317764410902747343693606214552320833068586707310148135874779120546511782981626423061122875113555547479538132213571579703426


solution = 693273491941638452870395399734960662527830094436
start = 248492895719275718569476604052405355739101691263412736004134252211412074288030991099191207760342640338883257179851011400604578388008550192624610859331174283808

assert ((start * 2 ** (8 * 20) + solution) ** e - enc) % N == 0

P.<x> = Zmod(N)[]
f = (start * 2 ** (8 * 20) + x) ^ 3 - enc
print(f.small_roots(beta=0.9))