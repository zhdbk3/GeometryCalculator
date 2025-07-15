export interface DomainSettings {
  negative: boolean;
  zero: boolean;
  positive: boolean;
}

export interface LatexItem {
  id: string;
  latex: string;
}

export type Status = [boolean, string];

export type AddBinCondFunc = (input1: string, input2: string) => Promise<Status>;

declare global {
  interface Window {
    pywebview: {
      api: {
        problem: {
          add_symbol(name: string, domain_settings: DomainSettings);
          add_point(
            name: string,
            x_str: string,
            y_str: string,
            line1: string,
            line2: string,
          ): Promise<Status>;
          add_expr_eq: AddBinCondFunc;
          add_parallel: AddBinCondFunc;
          add_perp: AddBinCondFunc;
          add_cong: AddBinCondFunc;
          add_sim: AddBinCondFunc;

          get_symbol_names(): Promise<Array<string>>;
          get_point_names(): Promise<Array<string>>;

          get_symbols_latex(): Promise<Array<LatexItem>>;
          get_points_latex(): Promise<Array<LatexItem>>;
          get_conds_latex(): Promise<Array<LatexItem>>;
        };
      };
    };
  }
}
