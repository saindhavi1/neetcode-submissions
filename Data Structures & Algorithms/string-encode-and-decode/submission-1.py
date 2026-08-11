class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = "";
        for word in strs:
            answer += str(len(word)) + "#" + word
            
        print(answer);
        return answer;

    def decode(self, s: str) -> List[str]:
        answer = [];
        i = 0; 
        while i < len(s):
            j = i;
            # 5#Hello5#World
            while s[j] != "#":
                j+=1;
            start = j+1;
            end = start+int(s[i:j]);
            answer.append(s[start:end]);
            i = end;
        return answer;

            

        
