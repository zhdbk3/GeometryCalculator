export function wrapInline(latex: string) {
  return `$ ${latex} $`;
}

export function wrapBlock(latex: string) {
  return `$$ ${latex} $$`;
}
