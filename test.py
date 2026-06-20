from tabulate import tabulate

class Team:
    def __init__(self, code, country, wins, draws, goals_for, goals_against):
        self.code = code
        self.country = country
        self.wins = wins
        self.draws = draws
        self.goals_for = goals_for
        self.goals_against = goals_against

        self.goal_difference = 0
        self.points = 0
        self.status = ""

        self.calculate_stats()
        self.evaluate_status()

    def calculate_stats(self):
        self.goal_difference = self.goals_for - self.goals_against
        self.points = (self.wins * 3) + (self.draws * 1)

    
    def evaluate_status(self):
        if self.points >= 7:
            self.status = "Chắc chắn đi tiếp"
        elif self.points >= 5:
            self.status = "Cơ hội cao"
        elif self.points >= 3:
            self.status = "Cần nỗ lực"
        else:
            self.status = "Nguy cơ bị loại"

class WorldCupManager:
    def __init__(self):
        self.team = []

    # hàm tìm kiếm chung:
    def find_by_code(self, code):
        for i in self.team:
            if i.code == code:
                return i
            
        return None

    def add_team(self):
        while True:
            code = input("Nhập mã đội: ").strip().upper()

            if not code:
                print("Mã đội không được để trống!")
                continue

            if self.find_by_code(code):
                print("Mã đội đã tồn tại!")
                continue

            break

        while True:
            country = input("Nhập quốc gia: ").strip().title()

            if not country:
                print("Quốc gia không được để trống!")
                continue

            break

        while True:
            try:
                wins = int(input("Nhập số trận thắng: "))

                if wins <= 0:
                    print("Số trận thắng phải lớn hơn 0!")
                    continue

                break

            except ValueError:
                print("Vui lòng nhập số trận hợp lệ!")

        while True:
            try:
                draws = int(input("Nhập số trận hòa: "))

                if draws <= 0:
                    print("Số trận hòa phải lớn hơn 0!")
                    continue

                break

            except ValueError:
                print("Vui lòng nhập số trận hợp lệ!")

        while True:
            try:
                goals_for = int(input("Nhập số bàn thắng: "))

                if goals_for <= 0:
                    print("Số bàn thắng phải lơn hơn 0!")
                    continue

                break

            except ValueError:
                print("Vui lòng nhập số bàn hợp lệ!")

        while True:
            try:
                goals_against = int(input("Nhập số bàn thua: "))

                if goals_against <= 0:
                    print("Số bàn thua phải lơn hơn 0!")
                    continue

                break

            except ValueError:
                print("Vui lòng nhập số bàn hợp lệ!")
        
        new_team = Team(
            code,
            country,
            wins,
            draws,
            goals_for,
            goals_against
        )

        self.team.append(new_team)

        print("Thêm đội hình mới thành công!")

    def show_table(self, team=None):
        # phục vụ tái sử dụng hàm ở case tìm kiếm
        if team is None:
            team = self.team


        if not team:
            print("Danh sách hiện đang trống!")
            return

        table = []

        for i in team:
            table.append([
                i.code,
                i.country,
                i.wins,
                i.draws,
                i.goals_for,
                i.goals_against,
                i.goal_difference,
                i.points,
                i.status
            ])

        print(
            tabulate(
                table,
                headers=[
                    "Mã đội",
                    "Quốc gia",
                    "Số trận thắng",
                    "Số trận hòa",
                    "Số bàn ghi được",
                    "Số bàn bị thủng lưới",
                    "Hiệu số bàn thắng bại",
                    "Tổng điếm số",
                    "Đánh giá cơ hội đi tiếp"
                ],
                tablefmt="grid"
            )
        )

    def update_match_result(self):
        code = input("Nhập mã đội cần cập nhật: ").upper()

        update = self.find_by_code(code)

        if not update:
            print("Mã đội không tồn tại!")
            return
        
        while True:
            try:
                wins = int(input("Nhập số trận thắng mới: "))

                if wins <= 0:
                    print("Số trận thắng phải lớn hơn 0!")
                    continue

                break

            except ValueError:
                print("Vui lòng nhập số trận hợp lệ!")

        while True:
            try:
                draws = int(input("Nhập số trận hòa mới: "))

                if draws <= 0:
                    print("Số trận hòa phải lớn hơn 0!")
                    continue

                break

            except ValueError:
                print("Vui lòng nhập số trận hợp lệ!")

        while True:
            try:
                goals_for = int(input("Nhập số bàn thắng mới: "))

                if goals_for <= 0:
                    print("Số bàn thắng phải lơn hơn 0!")
                    continue

                break

            except ValueError:
                print("Vui lòng nhập số bàn hợp lệ!")

        while True:
            try:
                goals_against = int(input("Nhập số bàn thua mới: "))

                if goals_against <= 0:
                    print("Số bàn thua phải lơn hơn 0!")
                    continue

                break

            except ValueError:
                print("Vui lòng nhập số bàn hợp lệ!")


        update.wins = wins
        update.draws = draws
        update.goals_for = goals_for
        update.goals_against = goals_against

        update.calculate_stats()
        update.evaluate_status()

        print("Cập nhật đội hình thành công!")
    
    def delete_team(self):
        code = input("Nhập mã đội muốn xóa: ").strip().upper()

        delete = self.find_by_code(code)

        if not delete:
            print("Mã đội không tồn tại!")
            return
        
        confirm = input("Bạn có chắc chắn muốn xóa đội bóng này không? (Y/N): ").strip().lower()

        if confirm == "n":
            print("Thao tác đã được hủy.")
        elif confirm == "y":
            self.team.remove(delete)
            print("Thao tác xóa thành công.")
        else:
            print("Lựa chọn không hợp lệ.")

    def search_team(self):
        find = input("Nhập tên quốc gia muốn tìm kiếm: ").strip().lower()

        result = []

        for team in self.team:
            if find in team.country.lower():
                result.append(team)

        if not result:
            print("Không tìm thấy đội bóng phù hợp!")
            return

        self.show_table(result)


wc = WorldCupManager()

wc.team.extend([
    Team("ARG", "Argentina", 2, 1, 8, 2),
    Team("VIE", "Việt Nam", 1, 2, 4, 3),
    Team("JPN", "Japan", 1, 0, 2, 1),
    Team("THA", "Thailand", 0, 2, 1, 3)
])

while True:
    print("""
================ WORLD CUP 2026 MENU ================​
1. Hiển thị bảng xếp hạng các đội bóng​
2. Thêm đội bóng mới​
3. Cập nhật số liệu trận đấu của đội bóng​
4. Xóa đội bóng khỏi danh sách​
5. Tìm kiếm đội bóng theo quốc gia​
6. Thoát hệ thống​
=====================================================
""")
    
    choice = input("Nhập lựa chọn của bạn: ")

    match choice:
        case  "1":
            wc.show_table()

        case "2":
            wc.add_team()

        case "3":
            wc.update_match_result()

        case "4":
            wc.delete_team()

        case "5":
            wc.search_team()

        case "6":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý dữ liệu World Cup 2026!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")