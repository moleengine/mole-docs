.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_@Global Scope:

@Global Scope
=============

**Category:** Core

Brief Description
-----------------

Global scope constants and variables.

Member Variables
----------------

- :ref:`AudioServer<class_audioserver>` **AS** - [AudioServer] singleton
- :ref:`AudioServer<class_audioserver>` **AudioServer** - [AudioServer] singleton
- :ref:`Geometry<class_geometry>` **Geometry** - [Geometry] singleton
- :ref:`Globals<class_globals>` **Globals** - [Globals] singleton
- :ref:`IP<class_ip>` **IP** - [IP] singleton
- :ref:`Input<class_input>` **Input** - [Input] singleton
- :ref:`InputMap<class_inputmap>` **InputMap** - [InputMap] singleton
- :ref:`Reference<class_reference>` **Marshalls** - [Marshalls] singleton
- :ref:`OS<class_os>` **OS** - [OS] singleton
- :ref:`PhysicsServer<class_physicsserver>` **PS** - [PhysicsServer] singleton
- :ref:`Physics2DServer<class_physics2dserver>` **PS2D** - [Physics2DServer] singleton
- :ref:`PathRemap<class_pathremap>` **PathRemap** - [PathRemap] singleton
- :ref:`Performance<class_performance>` **Performance** - [Performance] singleton
- :ref:`Physics2DServer<class_physics2dserver>` **Physics2DServer** - [Physics2DServer] singleton
- :ref:`PhysicsServer<class_physicsserver>` **PhysicsServer** - [PhysicsServer] singleton
- :ref:`ResourceLoader<class_resourceloader>` **ResourceLoader** - [ResourceLoader] singleton
- :ref:`ResourceSaver<class_resourcesaver>` **ResourceSaver** - [ResourceSaver] singleton
- :ref:`SpatialSoundServer<class_spatialsoundserver>` **SS** - [SpatialSoundServer] singleton
- :ref:`SpatialSound2DServer<class_spatialsound2dserver>` **SS2D** - [SpatialSound2DServer] singleton
- :ref:`SpatialSound2DServer<class_spatialsound2dserver>` **SpatialSound2DServer** - [SpatialSound2DServer] singleton
- :ref:`SpatialSoundServer<class_spatialsoundserver>` **SpatialSoundServer** - [SpatialSoundServer] singleton
- :ref:`TranslationServer<class_translationserver>` **TS** - [TranslationServer] singleton
- :ref:`TranslationServer<class_translationserver>` **TranslationServer** - [TranslationServer] singleton
- :ref:`VisualServer<class_visualserver>` **VS** - [VisualServer] singleton
- :ref:`VisualServer<class_visualserver>` **VisualServer** - [VisualServer] singleton

Numeric Constants
-----------------

- **MARGIN_LEFT** = **0** --- Left margin, used usually for :ref:`Control<class_control>` or :ref:`StyleBox<class_stylebox>` derived classes.
- **MARGIN_TOP** = **1** --- Top margin, used usually for :ref:`Control<class_control>` or :ref:`StyleBox<class_stylebox>` derived classes.
- **MARGIN_RIGHT** = **2** --- Right margin, used usually for :ref:`Control<class_control>` or :ref:`StyleBox<class_stylebox>` derived classes.
- **MARGIN_BOTTOM** = **3** --- Bottom margin, used usually for :ref:`Control<class_control>` or :ref:`StyleBox<class_stylebox>` derived classes.
- **VERTICAL** = **1** --- General vertical alignment, used usually for :ref:`Separator<class_separator>`, :ref:`ScrollBar<class_scrollbar>`, :ref:`Slider<class_slider>`, etc.
- **HORIZONTAL** = **0** --- General horizontal alignment, used usually for :ref:`Separator<class_separator>`, :ref:`ScrollBar<class_scrollbar>`, :ref:`Slider<class_slider>`, etc.
- **HALIGN_LEFT** = **0** --- Horizontal left alignment, usually for text-derived classes.
- **HALIGN_CENTER** = **1** --- Horizontal center alignment, usually for text-derived classes.
- **HALIGN_RIGHT** = **2** --- Horizontal right alignment, usually for text-derived classes.
- **VALIGN_TOP** = **0** --- Vertical top alignment, usually for text-derived classes.
- **VALIGN_CENTER** = **1** --- Vertical center alignment, usually for text-derived classes.
- **VALIGN_BOTTOM** = **2** --- Vertical bottom alignment, usually for text-derived classes.
- **SPKEY** = **16777216** --- Scancodes with this bit applied are non printable.
- **KEY_ESCAPE** = **16777217** --- Escape Key
- **KEY_TAB** = **16777218** --- Tab Key
- **KEY_BACKTAB** = **16777219** --- Shift-Tab Key
- **KEY_BACKSPACE** = **16777220** --- Backspace Key
- **KEY_RETURN** = **16777221** --- Return Key (On Main Keyboard)
- **KEY_ENTER** = **16777222** --- Enter Key (On Numpad)
- **KEY_INSERT** = **16777223** --- Insert Key
- **KEY_DELETE** = **16777224** --- Delete Key
- **KEY_PAUSE** = **16777225** --- Pause Key
- **KEY_PRINT** = **16777226** --- Printscreen Key
- **KEY_SYSREQ** = **16777227**
- **KEY_CLEAR** = **16777228**
- **KEY_HOME** = **16777229** --- Home Key
- **KEY_END** = **16777230** --- End Key
- **KEY_LEFT** = **16777231** --- Left Arrow Key
- **KEY_UP** = **16777232** --- Up Arrow Key
- **KEY_RIGHT** = **16777233** --- Right Arrow Key
- **KEY_DOWN** = **16777234** --- Down Arrow Key
- **KEY_PAGEUP** = **16777235** --- Pageup Key
- **KEY_PAGEDOWN** = **16777236** --- Pagedown Key
- **KEY_SHIFT** = **16777237** --- Shift Key
- **KEY_CONTROL** = **16777238** --- Control Key
- **KEY_META** = **16777239**
- **KEY_ALT** = **16777240** --- Alt Key
- **KEY_CAPSLOCK** = **16777241** --- Capslock Key
- **KEY_NUMLOCK** = **16777242** --- Numlock Key
- **KEY_SCROLLLOCK** = **16777243** --- Scrolllock Key
- **KEY_F1** = **16777244** --- F1 Key
- **KEY_F2** = **16777245** --- F2 Key
- **KEY_F3** = **16777246** --- F3 Key
- **KEY_F4** = **16777247** --- F4 Key
- **KEY_F5** = **16777248** --- F5 Key
- **KEY_F6** = **16777249** --- F6 Key
- **KEY_F7** = **16777250** --- F7 Key
- **KEY_F8** = **16777251** --- F8 Key
- **KEY_F9** = **16777252** --- F9 Key
- **KEY_F10** = **16777253** --- F10 Key
- **KEY_F11** = **16777254** --- F11 Key
- **KEY_F12** = **16777255** --- F12 Key
- **KEY_F13** = **16777256** --- F13 Key
- **KEY_F14** = **16777257** --- F14 Key
- **KEY_F15** = **16777258** --- F15 Key
- **KEY_F16** = **16777259** --- F16 Key
- **KEY_KP_ENTER** = **16777344** --- Enter Key on Numpad
- **KEY_KP_MULTIPLY** = **16777345** --- Multiply Key on Numpad
- **KEY_KP_DIVIDE** = **16777346** --- Divide Key on Numpad
- **KEY_KP_SUBTRACT** = **16777347** --- Subtract Key on Numpad
- **KEY_KP_PERIOD** = **16777348** --- Period Key on Numpad
- **KEY_KP_ADD** = **16777349** --- Add Key on Numpad
- **KEY_KP_0** = **16777350** --- Number 0 on Numpad
- **KEY_KP_1** = **16777351** --- Number 1 on Numpad
- **KEY_KP_2** = **16777352** --- Number 2 on Numpad
- **KEY_KP_3** = **16777353** --- Number 3 on Numpad
- **KEY_KP_4** = **16777354** --- Number 4 on Numpad
- **KEY_KP_5** = **16777355** --- Number 5 on Numpad
- **KEY_KP_6** = **16777356** --- Number 6 on Numpad
- **KEY_KP_7** = **16777357** --- Number 7 on Numpad
- **KEY_KP_8** = **16777358** --- Number 8 on Numpad
- **KEY_KP_9** = **16777359** --- Number 9 on Numpad
- **KEY_SUPER_L** = **16777260** --- Super Left key (windows key)
- **KEY_SUPER_R** = **16777261** --- Super Left key (windows key)
- **KEY_MENU** = **16777262** --- Context menu key
- **KEY_HYPER_L** = **16777263**
- **KEY_HYPER_R** = **16777264**
- **KEY_HELP** = **16777265** --- Help key
- **KEY_DIRECTION_L** = **16777266**
- **KEY_DIRECTION_R** = **16777267**
- **KEY_BACK** = **16777280** --- Back key
- **KEY_FORWARD** = **16777281** --- Forward key
- **KEY_STOP** = **16777282** --- Stop key
- **KEY_REFRESH** = **16777283** --- Refresh key
- **KEY_VOLUMEDOWN** = **16777284** --- Volume down key
- **KEY_VOLUMEMUTE** = **16777285** --- Mute volume key
- **KEY_VOLUMEUP** = **16777286** --- Volume up key
- **KEY_BASSBOOST** = **16777287**
- **KEY_BASSUP** = **16777288**
- **KEY_BASSDOWN** = **16777289**
- **KEY_TREBLEUP** = **16777290**
- **KEY_TREBLEDOWN** = **16777291**
- **KEY_MEDIAPLAY** = **16777292** --- Media play key
- **KEY_MEDIASTOP** = **16777293** --- Media stop key
- **KEY_MEDIAPREVIOUS** = **16777294** --- Previous song key
- **KEY_MEDIANEXT** = **16777295** --- Next song key
- **KEY_MEDIARECORD** = **16777296** --- Media record key
- **KEY_HOMEPAGE** = **16777297** --- Home page key
- **KEY_FAVORITES** = **16777298** --- Favorites key
- **KEY_SEARCH** = **16777299** --- Search key
- **KEY_STANDBY** = **16777300**
- **KEY_OPENURL** = **16777301**
- **KEY_LAUNCHMAIL** = **16777302**
- **KEY_LAUNCHMEDIA** = **16777303**
- **KEY_LAUNCH0** = **16777304**
- **KEY_LAUNCH1** = **16777305**
- **KEY_LAUNCH2** = **16777306**
- **KEY_LAUNCH3** = **16777307**
- **KEY_LAUNCH4** = **16777308**
- **KEY_LAUNCH5** = **16777309**
- **KEY_LAUNCH6** = **16777310**
- **KEY_LAUNCH7** = **16777311**
- **KEY_LAUNCH8** = **16777312**
- **KEY_LAUNCH9** = **16777313**
- **KEY_LAUNCHA** = **16777314**
- **KEY_LAUNCHB** = **16777315**
- **KEY_LAUNCHC** = **16777316**
- **KEY_LAUNCHD** = **16777317**
- **KEY_LAUNCHE** = **16777318**
- **KEY_LAUNCHF** = **16777319**
- **KEY_UNKNOWN** = **33554431**
- **KEY_SPACE** = **32** --- Space Key
- **KEY_EXCLAM** = **33** --- ! key
- **KEY_QUOTEDBL** = **34** --- " key
- **KEY_NUMBERSIGN** = **35** --- # key
- **KEY_DOLLAR** = **36** --- $ key
- **KEY_PERCENT** = **37** --- % key
- **KEY_AMPERSAND** = **38** --- & key
- **KEY_APOSTROPHE** = **39** --- ' key
- **KEY_PARENLEFT** = **40** --- ( key
- **KEY_PARENRIGHT** = **41** --- ) key
- **KEY_ASTERISK** = **42** --- \* key
- **KEY_PLUS** = **43** --- + key
- **KEY_COMMA** = **44** --- , key
- **KEY_MINUS** = **45** --- - key
- **KEY_PERIOD** = **46** --- . key
- **KEY_SLASH** = **47** --- / key
- **KEY_0** = **48** --- Number 0
- **KEY_1** = **49** --- Number 1
- **KEY_2** = **50** --- Number 2
- **KEY_3** = **51** --- Number 3
- **KEY_4** = **52** --- Number 4
- **KEY_5** = **53** --- Number 5
- **KEY_6** = **54** --- Number 6
- **KEY_7** = **55** --- Number 7
- **KEY_8** = **56** --- Number 8
- **KEY_9** = **57** --- Number 9
- **KEY_COLON** = **58** --- : key
- **KEY_SEMICOLON** = **59** --- ; key
- **KEY_LESS** = **60** --- Lower than key
- **KEY_EQUAL** = **61** --- = key
- **KEY_GREATER** = **62** --- Greater than key
- **KEY_QUESTION** = **63** --- ? key
- **KEY_AT** = **64** --- @ key
- **KEY_A** = **65** --- A Key
- **KEY_B** = **66** --- B Key
- **KEY_C** = **67** --- C Key
- **KEY_D** = **68** --- D Key
- **KEY_E** = **69** --- E Key
- **KEY_F** = **70** --- F Key
- **KEY_G** = **71** --- G Key
- **KEY_H** = **72** --- H Key
- **KEY_I** = **73** --- I Key
- **KEY_J** = **74** --- J Key
- **KEY_K** = **75** --- K Key
- **KEY_L** = **76** --- L Key
- **KEY_M** = **77** --- M Key
- **KEY_N** = **78** --- N Key
- **KEY_O** = **79** --- O Key
- **KEY_P** = **80** --- P Key
- **KEY_Q** = **81** --- Q Key
- **KEY_R** = **82** --- R Key
- **KEY_S** = **83** --- S Key
- **KEY_T** = **84** --- T Key
- **KEY_U** = **85** --- U Key
- **KEY_V** = **86** --- V Key
- **KEY_W** = **87** --- W Key
- **KEY_X** = **88** --- X Key
- **KEY_Y** = **89** --- Y Key
- **KEY_Z** = **90** --- Z Key
- **KEY_BRACKETLEFT** = **91** --- [ key
- **KEY_BACKSLASH** = **92** --- \ key
- **KEY_BRACKETRIGHT** = **93** --- ] key
- **KEY_ASCIICIRCUM** = **94** --- ^ key
- **KEY_UNDERSCORE** = **95** --- \_ key
- **KEY_QUOTELEFT** = **96**
- **KEY_BRACELEFT** = **123** --- { key
- **KEY_BAR** = **124** --- | key
- **KEY_BRACERIGHT** = **125** --- } key
- **KEY_ASCIITILDE** = **126** --- ~ key
- **KEY_NOBREAKSPACE** = **160**
- **KEY_EXCLAMDOWN** = **161**
- **KEY_CENT** = **162** --- ¢ key
- **KEY_STERLING** = **163**
- **KEY_CURRENCY** = **164**
- **KEY_YEN** = **165**
- **KEY_BROKENBAR** = **166** --- ¦ key
- **KEY_SECTION** = **167** --- § key
- **KEY_DIAERESIS** = **168** --- ¨ key
- **KEY_COPYRIGHT** = **169** --- © key
- **KEY_ORDFEMININE** = **170**
- **KEY_GUILLEMOTLEFT** = **171** --- « key
- **KEY_NOTSIGN** = **172** --- » key
- **KEY_HYPHEN** = **173** --- ‐ key
- **KEY_REGISTERED** = **174** --- ® key
- **KEY_MACRON** = **175**
- **KEY_DEGREE** = **176** --- ° key
- **KEY_PLUSMINUS** = **177** --- ± key
- **KEY_TWOSUPERIOR** = **178** --- ² key
- **KEY_THREESUPERIOR** = **179** --- ³ key
- **KEY_ACUTE** = **180** --- ´ key
- **KEY_MU** = **181** --- µ key
- **KEY_PARAGRAPH** = **182**
- **KEY_PERIODCENTERED** = **183** --- · key
- **KEY_CEDILLA** = **184** --- ¬ key
- **KEY_ONESUPERIOR** = **185**
- **KEY_MASCULINE** = **186**
- **KEY_GUILLEMOTRIGHT** = **187**
- **KEY_ONEQUARTER** = **188**
- **KEY_ONEHALF** = **189** --- ½ key
- **KEY_THREEQUARTERS** = **190**
- **KEY_QUESTIONDOWN** = **191**
- **KEY_AGRAVE** = **192**
- **KEY_AACUTE** = **193**
- **KEY_ACIRCUMFLEX** = **194**
- **KEY_ATILDE** = **195**
- **KEY_ADIAERESIS** = **196**
- **KEY_ARING** = **197**
- **KEY_AE** = **198**
- **KEY_CCEDILLA** = **199**
- **KEY_EGRAVE** = **200**
- **KEY_EACUTE** = **201**
- **KEY_ECIRCUMFLEX** = **202**
- **KEY_EDIAERESIS** = **203**
- **KEY_IGRAVE** = **204**
- **KEY_IACUTE** = **205**
- **KEY_ICIRCUMFLEX** = **206**
- **KEY_IDIAERESIS** = **207**
- **KEY_ETH** = **208**
- **KEY_NTILDE** = **209**
- **KEY_OGRAVE** = **210**
- **KEY_OACUTE** = **211**
- **KEY_OCIRCUMFLEX** = **212**
- **KEY_OTILDE** = **213**
- **KEY_ODIAERESIS** = **214**
- **KEY_MULTIPLY** = **215**
- **KEY_OOBLIQUE** = **216**
- **KEY_UGRAVE** = **217**
- **KEY_UACUTE** = **218**
- **KEY_UCIRCUMFLEX** = **219**
- **KEY_UDIAERESIS** = **220**
- **KEY_YACUTE** = **221**
- **KEY_THORN** = **222**
- **KEY_SSHARP** = **223**
- **KEY_DIVISION** = **247**
- **KEY_YDIAERESIS** = **255**
- **KEY_CODE_MASK** = **33554431**
- **KEY_MODIFIER_MASK** = **-16777216**
- **KEY_MASK_SHIFT** = **33554432**
- **KEY_MASK_ALT** = **67108864**
- **KEY_MASK_META** = **134217728**
- **KEY_MASK_CTRL** = **268435456**
- **KEY_MASK_CMD** = **268435456**
- **KEY_MASK_KPAD** = **536870912**
- **KEY_MASK_GROUP_SWITCH** = **1073741824**
- **BUTTON_LEFT** = **1** --- Left Mouse Button
- **BUTTON_RIGHT** = **2** --- Right Mouse Button
- **BUTTON_MIDDLE** = **3** --- Middle Mouse Button
- **BUTTON_WHEEL_UP** = **4** --- Mouse wheel up
- **BUTTON_WHEEL_DOWN** = **5** --- Mouse wheel down
- **BUTTON_WHEEL_LEFT** = **6** --- Mouse wheel left button
- **BUTTON_WHEEL_RIGHT** = **7** --- Mouse wheel right button
- **BUTTON_MASK_LEFT** = **1**
- **BUTTON_MASK_RIGHT** = **2**
- **BUTTON_MASK_MIDDLE** = **4**
- **JOY_BUTTON_0** = **0** --- Joystick Button 0
- **JOY_BUTTON_1** = **1** --- Joystick Button 1
- **JOY_BUTTON_2** = **2** --- Joystick Button 2
- **JOY_BUTTON_3** = **3** --- Joystick Button 3
- **JOY_BUTTON_4** = **4** --- Joystick Button 4
- **JOY_BUTTON_5** = **5** --- Joystick Button 5
- **JOY_BUTTON_6** = **6** --- Joystick Button 6
- **JOY_BUTTON_7** = **7** --- Joystick Button 7
- **JOY_BUTTON_8** = **8** --- Joystick Button 8
- **JOY_BUTTON_9** = **9** --- Joystick Button 9
- **JOY_BUTTON_10** = **10** --- Joystick Button 10
- **JOY_BUTTON_11** = **11** --- Joystick Button 11
- **JOY_BUTTON_12** = **12** --- Joystick Button 12
- **JOY_BUTTON_13** = **13** --- Joystick Button 13
- **JOY_BUTTON_14** = **14** --- Joystick Button 14
- **JOY_BUTTON_15** = **15** --- Joystick Button 15
- **JOY_BUTTON_MAX** = **16** --- Joystick Button 16
- **JOY_SNES_A** = **1** --- Super Nintendo Entertaiment System controller A button
- **JOY_SNES_B** = **0** --- Super Nintendo Entertaiment System controller B button
- **JOY_SNES_X** = **3** --- Super Nintendo Entertaiment System controller X button
- **JOY_SNES_Y** = **2** --- Super Nintendo Entertaiment System controller Y button
- **JOY_SONY_CIRCLE** = **1** --- DUALSHOCK circle button
- **JOY_SONY_X** = **0** --- DUALSHOCK X button
- **JOY_SONY_SQUARE** = **2** --- DUALSHOCK square button
- **JOY_SONY_TRIANGLE** = **3** --- DUALSHOCK triangle button
- **JOY_SEGA_B** = **1** --- SEGA controller B button
- **JOY_SEGA_A** = **0** --- SEGA controller A button
- **JOY_SEGA_X** = **2** --- SEGA controller X button
- **JOY_SEGA_Y** = **3** --- SEGA controller Y button
- **JOY_XBOX_B** = **1** --- XBOX controller B button
- **JOY_XBOX_A** = **0** --- XBOX controller A button
- **JOY_XBOX_X** = **2** --- XBOX controller X button
- **JOY_XBOX_Y** = **3** --- XBOX controller Y button
- **JOY_DS_A** = **1**
- **JOY_DS_B** = **0**
- **JOY_DS_X** = **3**
- **JOY_DS_Y** = **2**
- **JOY_SELECT** = **10** --- Joystick Button Select
- **JOY_START** = **11** --- Joystick Button Start
- **JOY_DPAD_UP** = **12** --- Joystick DPad Up
- **JOY_DPAD_DOWN** = **13** --- Joystick DPad Down
- **JOY_DPAD_LEFT** = **14** --- Joystick DPad Left
- **JOY_DPAD_RIGHT** = **15** --- Joystick DPad Right
- **JOY_L** = **4** --- Joystick Left Shoulder Button
- **JOY_L2** = **6** --- Joystick Left Trigger
- **JOY_L3** = **8** --- Joystick Left Stick Click
- **JOY_R** = **5** --- Joystick Right Shoulder Button
- **JOY_R2** = **7** --- Joystick Right Trigger
- **JOY_R3** = **9** --- Joystick Right Stick Click
- **JOY_AXIS_0** = **0** --- Joystick Left Stick Horizontal Axis
- **JOY_AXIS_1** = **1** --- Joystick Left Stick Vertical Axis
- **JOY_AXIS_2** = **2** --- Joystick Right Stick Horizontal Axis
- **JOY_AXIS_3** = **3** --- Joystick Right Stick Vertical Axis
- **JOY_AXIS_4** = **4**
- **JOY_AXIS_5** = **5**
- **JOY_AXIS_6** = **6** --- Joystick Left Trigger Analog Axis
- **JOY_AXIS_7** = **7** --- Joystick Right Trigger Analog Axis
- **JOY_AXIS_MAX** = **8**
- **JOY_ANALOG_0_X** = **0** --- Joystick Left Stick Horizontal Axis
- **JOY_ANALOG_0_Y** = **1** --- Joystick Left Stick Vertical Axis
- **JOY_ANALOG_1_X** = **2** --- Joystick Right Stick Horizontal Axis
- **JOY_ANALOG_1_Y** = **3** --- Joystick Right Stick Vertical Axis
- **JOY_ANALOG_2_X** = **4**
- **JOY_ANALOG_2_Y** = **5**
- **JOY_ANALOG_L2** = **6**
- **JOY_ANALOG_R2** = **7**
- **OK** = **0** --- Functions that return Error return OK when everything went ok. Most functions don't return error anyway and/or just print errors to stdout.
- **FAILED** = **1** --- Generic fail return error.
- **ERR_UNAVAILABLE** = **2**
- **ERR_UNCONFIGURED** = **3**
- **ERR_UNAUTHORIZED** = **4**
- **ERR_PARAMETER_RANGE_ERROR** = **5**
- **ERR_OUT_OF_MEMORY** = **6**
- **ERR_FILE_NOT_FOUND** = **7**
- **ERR_FILE_BAD_DRIVE** = **8**
- **ERR_FILE_BAD_PATH** = **9**
- **ERR_FILE_NO_PERMISSION** = **10**
- **ERR_FILE_ALREADY_IN_USE** = **11**
- **ERR_FILE_CANT_OPEN** = **12**
- **ERR_FILE_CANT_WRITE** = **13**
- **ERR_FILE_CANT_READ** = **14**
- **ERR_FILE_UNRECOGNIZED** = **15**
- **ERR_FILE_CORRUPT** = **16**
- **ERR_FILE_MISSING_DEPENDENCIES** = **17**
- **ERR_FILE_EOF** = **18**
- **ERR_CANT_OPEN** = **19**
- **ERR_CANT_CREATE** = **20**
- **ERR_PARSE_ERROR** = **43**
- **ERROR_QUERY_FAILED** = **21**
- **ERR_ALREADY_IN_USE** = **22**
- **ERR_LOCKED** = **23**
- **ERR_TIMEOUT** = **24**
- **ERR_CANT_AQUIRE_RESOURCE** = **28**
- **ERR_INVALID_DATA** = **30**
- **ERR_INVALID_PARAMETER** = **31**
- **ERR_ALREADY_EXISTS** = **32**
- **ERR_DOES_NOT_EXIST** = **33**
- **ERR_DATABASE_CANT_READ** = **34**
- **ERR_DATABASE_CANT_WRITE** = **35**
- **ERR_COMPILATION_FAILED** = **36**
- **ERR_METHOD_NOT_FOUND** = **37**
- **ERR_LINK_FAILED** = **38**
- **ERR_SCRIPT_FAILED** = **39**
- **ERR_CYCLIC_LINK** = **40**
- **ERR_BUSY** = **44**
- **ERR_HELP** = **46**
- **ERR_BUG** = **47**
- **ERR_WTF** = **49**
- **PROPERTY_HINT_NONE** = **0** --- No hint for edited property.
- **PROPERTY_HINT_RANGE** = **1** --- Hints that the string is a range, defined as "min,max" or "min,max,step". This is valid for integers and floats.
- **PROPERTY_HINT_EXP_RANGE** = **2** --- Hints that the string is an exponential range, defined as "min,max" or "min,max,step". This is valid for integers and floats.
- **PROPERTY_HINT_ENUM** = **3** --- Property hint for an enumerated value, like "Hello,Something,Else". This is valid for integer, float and string properties.
- **PROPERTY_HINT_EXP_EASING** = **4**
- **PROPERTY_HINT_LENGTH** = **5**
- **PROPERTY_HINT_KEY_ACCEL** = **7**
- **PROPERTY_HINT_FLAGS** = **8** --- Property hint for a bitmask description, for bits 0,1,2,3 and 5 the hint would be like "Bit0,Bit1,Bit2,Bit3,,Bit5". Valid only for integers.
- **PROPERTY_HINT_ALL_FLAGS** = **9** --- Property hint for a bitmask description that covers all 32 bits. Valid only for integers.
- **PROPERTY_HINT_FILE** = **10** --- String property is a file (so pop up a file dialog when edited). Hint string can be a set of wildcards like "\*.doc".
- **PROPERTY_HINT_DIR** = **11** --- String property is a directory (so pop up a file dialog when edited).
- **PROPERTY_HINT_GLOBAL_FILE** = **12**
- **PROPERTY_HINT_GLOBAL_DIR** = **13**
- **PROPERTY_HINT_RESOURCE_TYPE** = **14** --- String property is a resource, so open the resource popup menu when edited.
- **PROPERTY_HINT_MULTILINE_TEXT** = **15**
- **PROPERTY_HINT_COLOR_NO_ALPHA** = **16**
- **PROPERTY_HINT_IMAGE_COMPRESS_LOSSY** = **17**
- **PROPERTY_HINT_IMAGE_COMPRESS_LOSSLESS** = **18**
- **PROPERTY_USAGE_STORAGE** = **1** --- Property will be used as storage (default).
- **PROPERTY_USAGE_EDITOR** = **2** --- Property will be visible in editor (default).
- **PROPERTY_USAGE_NETWORK** = **4**
- **PROPERTY_USAGE_EDITOR_HELPER** = **8**
- **PROPERTY_USAGE_CHECKABLE** = **16**
- **PROPERTY_USAGE_CHECKED** = **32**
- **PROPERTY_USAGE_INTERNATIONALIZED** = **64**
- **PROPERTY_USAGE_BUNDLE** = **128**
- **PROPERTY_USAGE_CATEGORY** = **256**
- **PROPERTY_USAGE_STORE_IF_NONZERO** = **512**
- **PROPERTY_USAGE_STORE_IF_NONONE** = **1024**
- **PROPERTY_USAGE_NO_INSTANCE_STATE** = **2048**
- **PROPERTY_USAGE_RESTART_IF_CHANGED** = **4096**
- **PROPERTY_USAGE_SCRIPT_VARIABLE** = **8192**
- **PROPERTY_USAGE_DEFAULT** = **7** --- Default usage (storage and editor).
- **PROPERTY_USAGE_DEFAULT_INTL** = **71**
- **PROPERTY_USAGE_NOEDITOR** = **5**
- **METHOD_FLAG_NORMAL** = **1**
- **METHOD_FLAG_EDITOR** = **2**
- **METHOD_FLAG_NOSCRIPT** = **4**
- **METHOD_FLAG_CONST** = **8**
- **METHOD_FLAG_REVERSE** = **16**
- **METHOD_FLAG_VIRTUAL** = **32**
- **METHOD_FLAG_FROM_SCRIPT** = **64**
- **METHOD_FLAGS_DEFAULT** = **1**
- **TYPE_NIL** = **0** --- Variable is of type nil (only applied for null).
- **TYPE_BOOL** = **1** --- Variable is of type :ref:`bool<class_bool>`.
- **TYPE_INT** = **2** --- Variable is of type :ref:`int<class_int>`.
- **TYPE_REAL** = **3** --- Variable is of type :ref:`float<class_float>`/real.
- **TYPE_STRING** = **4** --- Variable is of type :ref:`String<class_string>`.
- **TYPE_VECTOR2** = **5** --- Variable is of type :ref:`Vector2<class_vector2>`.
- **TYPE_RECT2** = **6** --- Variable is of type :ref:`Rect2<class_rect2>`.
- **TYPE_VECTOR3** = **7** --- Variable is of type :ref:`Vector3<class_vector3>`.
- **TYPE_MATRIX32** = **8** --- Variable is of type :ref:`Matrix32<class_matrix32>`.
- **TYPE_PLANE** = **9** --- Variable is of type :ref:`Plane<class_plane>`.
- **TYPE_QUAT** = **10** --- Variable is of type :ref:`Quat<class_quat>`.
- **TYPE_AABB** = **11** --- Variable is of type :ref:`AABB<class_aabb>`.
- **TYPE_MATRIX3** = **12** --- Variable is of type :ref:`Matrix3<class_matrix3>`.
- **TYPE_TRANSFORM** = **13** --- Variable is of type :ref:`Transform<class_transform>`.
- **TYPE_COLOR** = **14** --- Variable is of type :ref:`Color<class_color>`.
- **TYPE_IMAGE** = **15** --- Variable is of type :ref:`Image<class_image>`.
- **TYPE_NODE_PATH** = **16** --- Variable is of type :ref:`NodePath<class_nodepath>`.
- **TYPE_RID** = **17** --- Variable is of type :ref:`RID<class_rid>`.
- **TYPE_OBJECT** = **18** --- Variable is of type :ref:`Object<class_object>`.
- **TYPE_INPUT_EVENT** = **19** --- Variable is of type :ref:`InputEvent<class_inputevent>`.
- **TYPE_DICTIONARY** = **20** --- Variable is of type :ref:`Dictionary<class_dictionary>`.
- **TYPE_ARRAY** = **21** --- Variable is of type :ref:`Array<class_array>`.
- **TYPE_RAW_ARRAY** = **22**
- **TYPE_INT_ARRAY** = **23**
- **TYPE_REAL_ARRAY** = **24**
- **TYPE_STRING_ARRAY** = **25**
- **TYPE_VECTOR2_ARRAY** = **26**
- **TYPE_VECTOR3_ARRAY** = **27**
- **TYPE_COLOR_ARRAY** = **28**
- **TYPE_MAX** = **29**

Description
-----------

Global scope constants and variables. This is all that resides in the globals, constants regarding error codes, scancodes, property hints, etc. It's not much.

Singletons are also documented here, since they can be accessed from anywhere.

