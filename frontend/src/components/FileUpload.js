import React, { useState } from 'react';
import axios from 'axios';

const TwoSignatureVerification = () => {
    const [files, setFiles] = useState({ file1: null, file2: null });
    const [filePreviews, setFilePreviews] = useState({ file1Preview: '', file2Preview: '' }); // To store image previews
    const [result, setResult] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleFileChange = (e, fileKey) => {
        const selectedFile = e.target.files[0];
        if (selectedFile && !['image/jpeg', 'image/png'].includes(selectedFile.type)) {
            alert('Please upload a valid image file (JPEG/PNG).');
            setFiles((prev) => ({ ...prev, [fileKey]: null }));
        } else {
            setFiles((prev) => ({
                ...prev,
                [fileKey]: selectedFile,
                [`${fileKey}Name`]: selectedFile.name,
            }));

            // Image preview logic
            const fileReader = new FileReader();
            fileReader.onloadend = () => {
                setFilePreviews((prev) => ({
                    ...prev,
                    [`${fileKey}Preview`]: fileReader.result,
                }));
            };
            if (selectedFile) {
                fileReader.readAsDataURL(selectedFile);
            }

            setError('');
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!files.file1 || !files.file2) {
            alert('Please upload both signature images.');
            return;
        }

        const formData = new FormData();
        formData.append('file1', files.file1);
        formData.append('file2', files.file2);
        formData.append('file1Name', files.file1Name);
        formData.append('file2Name', files.file2Name);

        setLoading(true);
        setResult('');
        setError('');

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/verify-signatures/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setResult(response.data.result);
        } catch (err) {
            console.error('Error:', err);
            setError('Failed to verify the signatures.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container">
            <h2 className="header">Two Signature Verification</h2>
            <form onSubmit={handleSubmit}>
                <div className="upload-section">
                    <label>
                        Upload Signature 1:
                        <input
                            type="file"
                            onChange={(e) => handleFileChange(e, 'file1')}
                        />
                    </label>
                    {files.file1 && (
                        <div>
                            <p>File 1: {files.file1Name}</p>
                            <img src={filePreviews.file1Preview} alt="File 1 Preview" width="150" />
                        </div>
                    )}
                </div>
                <div className="upload-section">
                    <label>
                        Upload Signature 2:
                        <input
                            type="file"
                            onChange={(e) => handleFileChange(e, 'file2')}
                        />
                    </label>
                    {files.file2 && (
                        <div>
                            <p>File 2: {files.file2Name}</p>
                            <img src={filePreviews.file2Preview} alt="File 2 Preview" width="150" />
                        </div>
                    )}
                </div>
                <button type="submit" disabled={loading}>
                    {loading ? 'Verifying...' : 'Upload and Verify'}
                </button>
            </form>
            {loading && <p>Processing your request...</p>}
            {result && <h3 className="result success">{result}</h3>}
            {error && <h3 className="result error">{error}</h3>}
        </div>
    );
};

export default TwoSignatureVerification;
