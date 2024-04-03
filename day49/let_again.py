    def getConcatenation(self, nums: List[int]) -> List[int]:
        lista = []
        for i in (nums * 2):
            lista.append(i)
        return lista