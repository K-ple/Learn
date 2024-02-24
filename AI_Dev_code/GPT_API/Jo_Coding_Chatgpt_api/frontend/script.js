async function sendForuneRequest() {
    const url = 'http://localhost:3000/fortuneTell';
    const requestButton = document.getElementById('requestButton');
    const fortuneOutput = document.getElementById('fortuneOutput');

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: 'John' }),
        });

        if (response.ok) {
            const data = await response.json();
            fortuneOutput.textContent = '운세: ' + data.fortune;
        } else {
            console.error('서버 응답이 실패했습니다.', response.status);
        }

    } catch (error) {
        console.error('운세를 가져오는 동안 에러가 발생했습니다:', error);
    }
}

const requestButton = document.getElementById('requestButton');
requestButton.addEventListener('click', sendForuneRequest);