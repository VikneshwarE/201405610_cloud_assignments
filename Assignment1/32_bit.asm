.cfi_startproc
pushl	%ebp
.cfi_def_cfa_offset 8
.cfi_offset 5, -8
movl	%esp, %ebp
.cfi_def_cfa_register 5
andl	$-16, %esp
subl	$16, %esp
movl	$9, 8(%esp)
movl	$.LC0, 4(%esp)
movl	$1, (%esp)
call	__printf_chk
xorl	%eax, %eax
leave
.cfi_restore 5
.cfi_def_cfa 4, 4
ret
.cfi_endproc
