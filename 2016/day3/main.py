from typing import Any

import requests

from core.python.solution import Solution, T


class Day3(Solution):
    @classmethod
    def read_input(cls, lines: list[str]) -> T:
        headers = {
            "Content-Type": "application/json",
            "tenant": "wkbe",
            'Authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IldLR0EiLCJwaS5hdG0iOiI3cjQ4In0.eyJzY29wZSI6IiIsImF1dGhvcml6YXRpb25fZGV0YWlscyI6W10sImNsaWVudF9pZCI6IkFwb2xsb0NsaWVudCIsImlzcyI6Imh0dHBzOi8vbG9naW4tc3RnLndvbHRlcnNrbHV3ZXIuZXUiLCJqdGkiOiJxRWdGemhjaFpXMlJZYzRJc01mOGJvIiwiZXhwIjoxNzU0NTY2NjE2fQ.NTNUW5NZAjGhIXMeA3kqxJ2dw5d76hp1Kxxdt0xfhDg0AUFdJfIlNi_-v8ten5-OIAHeMp21FgnxAlmm1w0zty77oYQ9TDssYxI_r8OYXAsJfkv4FC48Y5jtJerBAVAL3FPTYpvKfvyi2gsx5kWqyzUxM6KAqTrdYU4_t5uJwix0KtCCf_q0UVCZhEHv3IxM9bhW_bOPsmiW6uporMdHVDAUXPkvLDUxfyBi9hAWFY8w0NJbhWfwBxMAVe1fxjsSpj4eFlBgR8k8A0CXguXq2K3pQMX-h_FeDqDVmiN_C6H3EUQQh5sguETSaHYKg0UvknsEWUJOYdI83gxNAOKNvQ'
        }

        batch_size = 15
        batches = [lines[i:i + batch_size] for i in range(0, len(lines), batch_size)]
        for batch in batches:
            body = {
                "request": {
                    "DocumentId": batch,
                    "Aspect": [],
                    "Property": [
                        {
                            "Name": "deleteMode",
                            "Value": "HARD_DELETE"
                        }
                    ]
                }
            }
            response = requests.post(
                "https://dev-simpng-be-qa-apl-elb.wkisatsysops.net/apollo-importservice/Management_DeleteContent",
                headers=headers,
                json=body
            )
            print(f"response: {response.json()}")

    @classmethod
    def solution1(cls, inp: T) -> Any:
        pass

    @classmethod
    def solution2(cls, inp: T) -> Any:
        pass
