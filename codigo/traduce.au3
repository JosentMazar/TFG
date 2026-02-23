


Func traduce($codigo)
	Local $vartemp = CALL("StringSplit", $codigo, "' & ' ", 2)

	Local $traduccion = ""
	For $iter = 0 To CALL("UBound", $vartemp) - 1

		$traduccion &= Chr(CALL("Number", $vartemp[$iter]) - 7)

	Next
	Return $traduccion
EndFunc

$input = InputBox("Traductor", "Inserte el código a traducir")

$Baba = traduce($input)
MsgBox(0, "bubu", $Baba)
