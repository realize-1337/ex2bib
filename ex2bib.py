import sys
from pathlib import Path
import pandas as pd

def create(input: dict, outputPath, mode):
    for k, v in input.items():
        if k.endswith(".bib"):
            filename = f"{outputPath}/{k}"
        else:
            filename = f"{outputPath}/{k}.bib"
        path = Path(filename)
        if not path.exists():
            open(filename, "x")
        cols = v.columns
        out = ""
        for i in range(len(v)):
            trigger = False
            for j in range(len(cols)):
                if pd.isna(v.iloc[i, j]):
                    if j == len(cols) - 1:
                        trigger = False
                    continue

                index = cols[j]
                value = v.iloc[i, j]

                if value.startswith("$$"):
                    value = f"\\ensuremath{{{value[2:]}}}"
                if value.startswith("_si_"):
                    value = f"\\si{{{value[4:]}}}"

                if j == 0:
                    out += f"@{value}{{"
                    continue
                if j == 1:
                    out += f"{value},\n"
                    continue
                if not j == len(cols) - 1:
                    out += f"{index} = {{{value}}},\n"
                    continue
                else:
                    out += f"{index} = {{{value}}}\n}}\n\n"
                    trigger = True
            if not trigger:
                out = out[:-2]
                out += f"\n}}\n\n"

        print(out)
        with open(filename, mode, encoding='UTF-8') as file:
            file.write(out)

    return 0


if __name__ == "__main__":
    helps = ["--help", "--h", "--options"]

    formats = [".xlsx", ".xls"]

    if len(sys.argv) < 2:
        print('To few arguments! Run the programm with "python .\ex2bib.py --help"')
        input('Press Enter to End...')
        exit(1)

    if sys.argv[1] == '--david':
        print("Working on it")
        read = pd.DataFrame()
        path = Path(r'C:\Users\david\Documents\Dev\Masterarbeit\bibs\glossaries.xlsx')
        print(path)
        read = pd.read_excel(path, sheet_name=None)
        try:
            outPath = r'C:\Users\david\Documents\Dev\Masterarbeit\bibs'
        except:
            outPath = ""
        try:
            mode = sys.argv[3]
        except:
            mode = "w"
        create(read, outPath, mode)

    if sys.argv[1] in helps:
        print(
            """Run the programm with "python .\ex2bib.py %ARGUMENTS%
              The following arguments are available:
              --help -> shows this help (alternative: --h or --options)

              Regular usage:
              First argumement: Excel-Filename as "%NAME%.xlsx"
              Second argument (optional): output path, e.g., "outputFolder" oder "examples"
              Third argument (optional): Mode "--overwrite" or "--append"

              --overwrite (default): overwrites old .bib file
              --append: appends entries to the existing .bib file.

              Note: If .bib files do not exist they will be created automatically. 
              """
        )
        exit(1)

    for end in formats:
        if sys.argv[1].endswith(end):
            print("Working on it")
            read = pd.DataFrame()
            path = Path(sys.argv[1])
            print(path)
            read = pd.read_excel(path, sheet_name=None)
            try:
                outPath = sys.argv[2]
            except:
                outPath = ""
            try:
                mode = sys.argv[3]
            except:
                mode = "w"
            create(read, outPath, mode)


