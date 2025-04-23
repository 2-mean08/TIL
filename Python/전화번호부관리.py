#전화번호부관리 프로그램2.0

class PhoneNumberManager:
    def __init__(self):
        self.phone_book = []

    # 중복 체크 후 신규 사용자 추가
    def add_user(self):
        name = input("이름: ")
        if self.find_user(name) is not None:
            print("이미 저장된 이름입니다.")
            return
        phone = input("전화번호: ")
        self.phone_book.append({"name": name, "phone": phone})
        print("저장완료")

    # 특정 사용자 위치 찾기
    def find_user(self, name):
        for index, entry in enumerate(self.phone_book):
            if entry["name"] == name:
                return index
        return None

    # 이름으로 검색하여 전화번호 수정
    def edit_user_info(self):
        name = input("수정할 이름을 입력하세요: ")
        position = self.find_user(name)
        if position is None:
            print("존재하지 않는 이름입니다.")
            return
        new_phone = input("수정할 전화번호 입력: ")
        self.phone_book[position]["phone"] = new_phone
        print("전화번호가 수정되었습니다.")

    # 특정 사용자 삭제
    def delete_user(self):
        name = input("삭제할 이름을 입력하세요: ")
        position = self.find_user(name)
        if position is None:
            print("존재하지 않는이름입니다.")
            return
        del self.phone_book[position]
        print("정보가 삭제되었습니다.")

    # 전체 전화번호 출력
    def print_all_phone_number(self):
        print("*" * 10, "전화번호부", "*" * 10)
        for entry in self.phone_book:
            print(f"이름: {entry['name']:5s}   전화번호: {entry['phone']:5s}")
        print("*" * 32)

    # 프로그램 실행 메서드
    def run(self):
        while True:
            choice = input("사용자 추가(n), 수정(e), 삭제(d), 전체 출력(p), 종료(q): ")

            if choice == 'n':
                self.add_user()
            elif choice == 'e':
                self.edit_user_info()
            elif choice == 'd':
                self.delete_user()
            elif choice == 'p':
                self.print_all_phone_number()
            elif choice == 'q':
                break
            else:
                print("다시 입력하세요.")

        print("\n프로그램을 종료합니다.")


# main part
if __name__ == '__main__':
    manager = PhoneNumberManager()
    manager.run()
