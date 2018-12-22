/*
 * テンプレート例
 */
.file "${func_name}.S"
.text
    .align  2
    .global ${func_name}
${func_name}:
    stmfd sp!, {r4-r7, r9, lr}

    # ${Comment}
    ${op1} ${Rd}, ${Rn}, ${Operand2}

    ldmfd sp!, {r4-r7, r9, pc} 
