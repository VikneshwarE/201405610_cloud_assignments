.cfi_startproc
subq	$8, %rsp
.cfi_def_cfa_offset 16
movl	$9,%edx
movl	$.LC0,%esi
movl	$1,%edi
xorl	%eax, %eax
call	__printf_chk
xorl	%eax, %eax
addq	$8, %rsp
.cfi_def_cfa_offset 8
ret
.cfi_endproc
